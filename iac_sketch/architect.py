from . import data
from . import parse


class Architect:

    def __init__(
        self,
        input_dir: str,
    ):
        self.input_dir = input_dir
        self.parser = parse.Parser(input_dir)

    def parse(self):

        self.parser.extract()
        self.parser.transform()
        self.comps = self.parser.comps
