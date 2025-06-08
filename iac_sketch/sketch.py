from . import etl, validate
from .etl import ExtractSystem, TransformSystem
import typing


class Architect:

    def __init__(
        self,
        input_dir: str,
        extract_sys: etl.ExtractSystem = None,
        transform_sys: etl.TransformSystem = None,
        valid_sys: validate.ValidationSystem = None,
    ):
        self.input_dir = input_dir
        self.extract_sys = extract_sys if extract_sys else etl.ExtractSystem()
        self.transform_sys = transform_sys if transform_sys else etl.TransformSystem()
        self.valid_sys = valid_sys if valid_sys else validate.ValidationSystem()

    def perform_registry_etl(
        self,
        input_paths: list[str],
        user_transforms: typing.Optional[typing.List[typing.Callable]] = None,
    ):
        """
        Main ETL workflow: extract, load, preprocess, system transforms, user transforms.
        """
        registry = self.extract_sys.extract_entities(input_paths)
        registry = self.transform_sys.apply_preprocess_transforms(registry)
        registry = self.transform_sys.apply_system_transforms(registry)
        if user_transforms:
            registry = self.transform_sys.apply_transforms(registry, user_transforms)
        return registry