import glob
import os

import yaml

class Parser:

    def __init__(self, dir: str):
        self.dir = dir

    def load(self):

        self.entities = {}
        for filename in glob.glob("*.yaml"):
            self.entities.upate(yaml.safe_load(filename))