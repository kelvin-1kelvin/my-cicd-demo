# NPG_test_temp.py  (Cloud Computing - Session 12: CI/CD - automating the
# path to production - STUDENT reproduce guide version)
# ============================================================================
# Unit tests for NPG_temp.py. These are what your pipeline's "test" job will
# run automatically on every push.
#
# Run directly with:
#     python -m unittest NPG_test_temp
# ============================================================================
import unittest

from NPG_temp import category


class TestCategory(unittest.TestCase):

    def test_well_below_cold_boundary(self):
        self.assertEqual(category(5), "Cold")

    def test_just_below_mild_boundary(self):
        self.assertEqual(category(14), "Cold")

    def test_fifteen_is_mild(self):
        self.assertEqual(category(15), "Mild")

    def test_just_below_hot_boundary(self):
        self.assertEqual(category(27), "Mild")

    def test_twenty_eight_is_hot(self):
        self.assertEqual(category(28), "Hot")

    def test_well_above_hot_boundary(self):
        self.assertEqual(category(40), "Hot")


if __name__ == "__main__":
    unittest.main()
