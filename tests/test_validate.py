import unittest

from iac_sketch import sketch, validate


class TestValidator(unittest.TestCase):
    def setUp(self):
        self.test_data_dir = "./public/components"
        self.valid_sys = validate.ValidationSystem()
        self.architect = sketch.Architect(
            self.test_data_dir,
            valid_sys=self.valid_sys,
        )
        self.registry = self.architect.parse()

    def test_validate_requirements(self):

        invalid_reqs = self.valid_sys.validate_requirements(self.registry)

        assert invalid_reqs.empty

    def test_validate_tasks(self):

        invalid_tasks = self.valid_sys.validate_tasks(self.registry)

        assert invalid_tasks.empty

    def test_validate_testcases(self):

        invalid_testcases = self.valid_sys.validate_testcases(self.registry)

        assert invalid_testcases.empty

    def test_validate_components(self):

        invalid_components = self.valid_sys.validate_components(self.registry)

        assert invalid_components.empty

    def test_validate_connectivity(self):

        invalid_entities = self.valid_sys.validate_connectivity(
            self.registry
        )

        assert invalid_entities.empty
