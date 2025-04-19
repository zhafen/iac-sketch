import glob

import yaml


class Parser:

    def __init__(self, input_dir: str):
        self.input_dir = input_dir

    def extract(self):

        self.entities = {}
        for filename in glob.glob(f"{self.input_dir}/*.yaml"):
            with open(filename, 'r', encoding='utf-8') as file:
                file_entities = yaml.safe_load(file)
            self.entities.update(file_entities)

    def transform(self):
        self.components = {
            "entity": [],
        }
        for entity, comps in self.entities.items():
            for i, entry in enumerate(comps):

                forrmat_error = ValueError(
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
                        raise forrmat_error
                    comp_entity, comp = list(entry.items())[0]
                # We should only have dictionaries or strings
                else:
                    raise forrmat_error

                # Create the component
                parsed = self.parse_component(comp_entity, comp)

                self.components["entity"].append(
                    {
                        "entity": entity,
                        "entity_ind": i,
                        "component": comp_entity,
                        "parsed": parsed,
                    }
                )

    def parse_component(self, comp_entity: str, comp: dict) -> bool:
        
        # Look for the function to parse the entity
        parse_fn = f"parse_component_{comp_entity}"
        if not hasattr(self, parse_fn):
            return False

        return getattr(self, parse_fn)(comp)