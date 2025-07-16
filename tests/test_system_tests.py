import unittest

from iac_sketch import sketch, system_tests


class TestSystemTests(unittest.TestCase):
    def setUp(self):
        architect = sketch.Architect()
        self.registry = architect.perform_registry_etl()

    def test_fully_designed(self):

        invalid_reqs = system_tests.test_designed(self.registry)

        assert invalid_reqs.empty

    def test_fully_implemented(self):

        invalid_reqs = system_tests.test_implemented(self.registry)

        assert invalid_reqs.empty

    def test_fully_defined(self):

        invalid_reqs = system_tests.test_defined(self.registry)

        assert invalid_reqs.empty

    def test_fully_connected(self):

        invalid_reqs = system_tests.test_connected(self.registry)

        assert invalid_reqs.empty