from . import parse, validate


class Architect:

    def __init__(
        self,
        input_dir: str,
        parse_sys: parse.ParseSystem = None,
        valid_sys: validate.ValidationSystem = None,
    ):
        self.input_dir = input_dir
        self.parse_sys = parse_sys if parse_sys else parse.ParseSystem()
        self.valid_sys = valid_sys if valid_sys else validate.ValidationSystem()

    def parse(self):

        self.registry = self.parse_sys.parse(self.input_dir)

        return self.registry