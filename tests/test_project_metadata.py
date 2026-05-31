import unittest

import opentaxai


class ProjectMetadataTest(unittest.TestCase):
    def test_version_is_exposed(self):
        self.assertEqual(opentaxai.__version__, "0.1.0")


if __name__ == "__main__":
    unittest.main()
