import unittest

from iac_sketch import sketch, validate


class TestValidator(unittest.TestCase):
    def setUp(self):
        self.valid_sys = validate.ValidationSystem()
        self.architect = sketch.Architect(valid_sys=self.valid_sys)
        self.architect.perform_registry_etl()
        
    def test_validate(self):

        is_valid, invalids = self.valid_sys.validate(self.architect.registry)

        assert is_valid
        for value in invalids.values():
            assert value.empty

    def test_validate_requirements(self):

        invalid_reqs = self.valid_sys.validate_requirements(self.architect.registry)

        assert invalid_reqs.empty

    def test_validate_tasks(self):

        invalid_tasks = self.valid_sys.validate_tasks(self.architect.registry)

        assert invalid_tasks.empty

    def test_validate_testcases(self):

        invalid_testcases = self.valid_sys.validate_testcases(self.architect.registry)

        assert invalid_testcases.empty

    def test_validate_components(self):

        invalid_components = self.valid_sys.validate_components(self.architect.registry)

        assert invalid_components.empty

    def test_validate_connectivity(self):

        invalid_entities = self.valid_sys.validate_connectivity(self.architect.registry)

        assert invalid_entities.empty


class TestValidatorRAExample(TestValidator):
    def setUp(self):
        self.valid_sys = validate.ValidationSystem()
        self.architect = sketch.Architect(
            filename_patterns="public/components/*.yaml", valid_sys=self.valid_sys
        )
        self.architect.perform_registry_etl()
