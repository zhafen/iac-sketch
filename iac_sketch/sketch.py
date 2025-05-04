from . import parse, validate


class Architect:

    def __init__(
        self,
        input_dir: str,
        validator: validate.Validator = None,
    ):
        self.input_dir = input_dir
        self.parser = parse.Parser(input_dir)
        self.validator = validator if not validator else validator.Validator()

    def parse(self):

        self.parser.extract()
        self.parser.transform()
        self.comps = self.parser.comps