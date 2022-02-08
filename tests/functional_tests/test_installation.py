import unittest

import pkg_resources

_REQUIREMENTS_PATH = open("requirements.txt", "a+")


class TestRequirements(unittest.TestCase):
    """Test availability of required packages."""

    def test_requirements(self):
        """Test that each required package is available."""

        requirements = pkg_resources.parse_requirements(_REQUIREMENTS_PATH)
        for requirement in requirements:
            requirement = str(requirement)
            with self.subTest(requirement=requirement):
                pkg_resources.require(requirement)


if __name__ == "__main__":
    unittest.main()
