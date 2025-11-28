"""
YAML writing functionality for serializing registry components to YAML files.
"""
import os
from collections import defaultdict

import numpy as np
import pandas as pd
import yaml


class YAMLWriter:
    """Main class that handles writing registry components to YAML files."""

    def __init__(self):
        pass

    def write_registry(
        self,
        registry,
        output_dir: str,
        organize_by_file: bool = True,
        filter_system_entities: bool = True,
    ) -> None:
        """Write registry components to YAML files.
        
        Parameters
        ----------
        registry : data.Registry
            The registry to write
        output_dir : str
            Directory to write YAML files to
        organize_by_file : bool
            If True, organize entities by their source filename.
            If False, write all entities to a single file.
        filter_system_entities : bool
            If True, only write user-defined entities (not system metadata).
            System entities include generated metadata like compdef, node, etc.
        """
        # Filter to user entities if requested
        if filter_system_entities and "entity_source" in registry:
            entity_sources = registry["entity_source"]
            user_entities = entity_sources[
                entity_sources["source"] == "user"
            ].index.get_level_values("entity").unique()
            
            # Filter compinst to only user entities
            compinst = registry["compinst"][
                registry["compinst"].index.get_level_values("entity").isin(
                    user_entities
                )
            ]
            entity_sources = entity_sources.loc[user_entities]
        else:
            # Get entity source information if available
            if "entity_source" in registry:
                entity_sources = registry["entity_source"]
            else:
                entity_sources = None
            
            # Get compinst to understand the structure
            compinst = registry["compinst"]

        # Group entities by their source file or create single output
        if organize_by_file and entity_sources is not None:
            entities_by_file = self._group_entities_by_file(
                compinst, entity_sources
            )
        else:
            # Put all entities in a single output file
            entities = compinst.index.get_level_values("entity").unique()
            entities_by_file = {"manifest.yaml": entities}

        # Write each file
        os.makedirs(output_dir, exist_ok=True)
        for filename, entities in entities_by_file.items():
            yaml_content = self._build_yaml_for_entities(
                registry, entities, compinst
            )
            
            # Create subdirectories if needed
            output_path = os.path.join(output_dir, filename)
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            with open(output_path, "w", encoding="utf-8") as f:
                yaml.dump(
                    yaml_content,
                    f,
                    default_flow_style=False,
                    sort_keys=False,
                    allow_unicode=True,
                )

    def _group_entities_by_file(self, compinst, entity_sources):
        """Group entities by their source filename."""
        entities_by_file = defaultdict(list)
        
        for entity in compinst.index.get_level_values("entity").unique():
            if entity in entity_sources.index:
                source_info = entity_sources.loc[entity]
                if isinstance(source_info, pd.DataFrame):
                    # Multiple sources, take the first
                    source_info = source_info.iloc[0]
                
                filename = source_info.get("filename", "manifest.yaml")
                if pd.notna(filename):
                    # Make relative to output
                    filename = os.path.basename(filename)
                else:
                    filename = "manifest.yaml"
            else:
                filename = "manifest.yaml"
            
            entities_by_file[filename].append(entity)
        
        return entities_by_file

    def _build_yaml_for_entities(self, registry, entities, compinst):
        """Build YAML structure for given entities.
        
        Parameters
        ----------
        registry : data.Registry
            The registry containing component data
        entities : list
            List of entity names to include
        compinst : pd.DataFrame
            Component instance tracking DataFrame
            
        Returns
        -------
        dict
            Dictionary suitable for YAML serialization
        """
        yaml_dict = {}
        
        for entity in entities:
            # Get all components for this entity
            entity_comps = compinst.loc[entity]
            if isinstance(entity_comps, pd.Series):
                entity_comps = entity_comps.to_frame().T
            
            components_list = []
            
            for _, comp_row in entity_comps.iterrows():
                comp_type = comp_row["component_type"]
                comp_key = comp_row.name if isinstance(comp_row.name, str) else comp_row.name[0]
                
                # Get the actual component data
                if comp_type in registry:
                    comp_df = registry[comp_type]
                    
                    # Try to find this specific component instance
                    if (entity, comp_key) in comp_df.index:
                        comp_data = comp_df.loc[(entity, comp_key)]
                    elif entity in comp_df.index:
                        # Single-valued component
                        comp_data = comp_df.loc[entity]
                        if isinstance(comp_data, pd.DataFrame):
                            comp_data = comp_data.iloc[0]
                    else:
                        # Component type exists but not for this entity
                        components_list.append(comp_type)
                        continue
                    
                    # Convert component data to dict
                    comp_dict = self._component_to_dict(comp_data)
                    
                    if comp_dict:
                        components_list.append({comp_type: comp_dict})
                    else:
                        components_list.append(comp_type)
                else:
                    # Component type doesn't exist in registry
                    components_list.append(comp_type)
            
            if components_list:
                yaml_dict[entity] = components_list
        
        return yaml_dict

    def _component_to_dict(self, comp_data):
        """Convert component Series to dict, filtering NaN values.
        
        Parameters
        ----------
        comp_data : pd.Series
            Component data as a Series
            
        Returns
        -------
        dict or None
            Dictionary representation of component, or None if only NaN values
        """
        if isinstance(comp_data, pd.Series):
            # Convert to dict and filter out NaN values
            comp_dict = {}
            for key, value in comp_data.items():
                # Skip internal registry fields
                if key in ['comp_key', 'entity']:
                    continue
                    
                # Convert numpy types to native Python types
                value = self._convert_to_native_type(value)
                
                # Handle different types of values
                if isinstance(value, (list, dict)):
                    # Always include lists and dicts (if not empty after filtering)
                    if value:  # Only include non-empty collections
                        comp_dict[key] = value
                elif isinstance(value, (int, float, str, bool)):
                    # Check for NaN on scalar types
                    if pd.notna(value):
                        comp_dict[key] = value
                elif value is not None:
                    # Include other non-None values
                    comp_dict[key] = value
            
            # If only "value" key exists, return just the value
            if len(comp_dict) == 1 and "value" in comp_dict:
                return comp_dict["value"]
            
            return comp_dict if comp_dict else None
        
        return None

    def _convert_to_native_type(self, value):
        """Convert numpy/pandas types to native Python types.
        
        Parameters
        ----------
        value : any
            Value to convert
            
        Returns
        -------
        any
            Converted value
        """
        # Skip complex objects that can't be serialized to YAML
        # These include Field objects, functions, etc.
        if hasattr(value, '__module__') and (
            'iaca.data' in str(value.__module__) or
            'pandera' in str(value.__module__) or
            callable(value)
        ):
            return None
            
        # Convert numpy types to native Python types
        if isinstance(value, np.integer):
            return int(value)
        elif isinstance(value, np.floating):
            return float(value)
        elif isinstance(value, np.bool_):
            return bool(value)
        elif isinstance(value, np.ndarray):
            return value.tolist()
        elif isinstance(value, (list, tuple)):
            converted = [self._convert_to_native_type(item) for item in value]
            # Filter out None values from complex objects
            return [item for item in converted if item is not None]
        elif isinstance(value, dict):
            converted = {
                k: self._convert_to_native_type(v) for k, v in value.items()
            }
            # Filter out None values from complex objects
            return {k: v for k, v in converted.items() if v is not None}
        return value
