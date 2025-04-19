import glob

import pandas as pd
import yaml


class Parser:

    def __init__(self, input_dir: str):
        self.input_dir = input_dir

    def extract(self):

        self.entities = []
        for filename in glob.glob(f"{self.input_dir}/*.yaml"):
            with open(filename, 'r', encoding='utf-8') as file:
                file_entities = yaml.safe_load(file)

                for entity, comps in file_entities.items():

                    # Check if the entity already exists
                    if entity in self.entities:
                        raise KeyError(
                            f"Entity {entity} is defined in multiple files."
                        )

                    self.entities += self.extract_entity(entity, comps)

        self.entities = pd.DataFrame(self.entities).set_index(("entity", "entity_ind"))

        return self.entities

    def extract_entity(self, entity: str, comps: list) -> list:

        extracted_comps = []
        for i, entry in enumerate(comps):
            format_error = ValueError(
                f"Entity component {entity}.{i} is not formatted correctly."
            )

            # When just given a flag
            if isinstance(entry, str):
                comp_entity = entry
                comp = {}
            # When given values for a component
            elif isinstance(entry, dict):
                # Check formatting
                if len(entry) != 1:
                    raise format_error
                comp_entity, comp = list(entry.items())[0]
            # We should only have dictionaries or strings
            else:
                raise format_error

            row = {
                "entity": entity,
                "entity_ind": i,
                "component_entity": comp_entity,
                "component": comp,
            }

        return extracted_comps

    def transform(self):
        self.components = {
            "entity": [],
        }
        for entity, comps in self.entities.items():
            for i, (comp_entity, comp) in enumerate(comps):

                # Create the component
                parsed = self.parse_component(comp_entity, comp, comps)

                self.components["entity"].append(
                    {
                        "entity": entity,
                        "entity_ind": i,
                        "component": comp_entity,
                        "parsed": parsed,
                    }
                )

    def parse_component(self, comp_entity: str, comp: dict, comps: list[]) -> bool:
        
        # Look for the function to parse the entity
        parse_fn = f"parse_component_{comp_entity}"
        if not hasattr(self, parse_fn):
            return False

        return getattr(self, parse_fn)(**comp)

    def parse_component_component(self):
        pass