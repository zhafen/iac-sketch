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