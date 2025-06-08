from . import parse, validate
from .etl import ExtractSystem, TransformSystem
import typing


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

    def perform_registry_etl(
        self,
        input_paths: list[str],
        user_transforms: typing.Optional[typing.List[typing.Callable]] = None,
    ):
        """
        Main ETL workflow: extract, load, preprocess, system transforms, user transforms.
        """
        extract = ExtractSystem()
        transform = TransformSystem()
        entities = extract.extract_entities(input_paths)
        registry = extract.load_entities_to_registry(entities)
        registry = transform.apply_preprocess_transforms(registry)
        registry = transform.apply_system_transforms(registry)
        if user_transforms:
            registry = transform.apply_transforms(registry, user_transforms)
        return registry