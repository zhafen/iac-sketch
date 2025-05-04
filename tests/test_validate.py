import unittest

from iac_sketch import sketch, validate


class TestValidator(unittest.TestCase):
    def setUp(self):
        self.test_data_dir = "./public/components"
        self.validator = validate.Validator()
        self.architect = sketch.Architect(
            self.test_data_dir,
            validator=self.validator,
        )
        self.architect.parse()

    def test_validate_requirements(self):

        self.validator.validate_requirements(self.architect.comps)