from . import parse, validate


class Architect:

    def __init__(
        self,
        input_dir: str,
        valid_sys: validate.ValidationSystem = None,
    ):
        self.input_dir = input_dir
        self.parse_sys = parse.ParseSystem(input_dir)
        self.valid_sys = valid_sys if not valid_sys else valid_sys.Validator()

    def parse(self):

        self.parse_sys.extract()
        self.parse_sys.transform()
        self.comps = self.parse_sys.comps