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
        self.architect.parse()

    def test_validate_requirements(self):

        invalid_reqs = self.valid_sys.validate_requirements(self.architect.comps)

        assert invalid_reqs.empty

    def test_validate_tasks(self):

        invalid_tasks = self.valid_sys.validate_tasks(self.architect.comps)

        assert invalid_tasks.empty

    def test_validate_connectivity(self):

        invalid_entities = self.valid_sys.validate_connectivity(
            self.architect.comps
        )

        assert invalid_entities.empty
