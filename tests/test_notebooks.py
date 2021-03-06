import os
import testipynb
import unittest

NBDIR = os.path.sep.join(
    os.path.abspath(__file__).split(os.path.sep)[:-2] + ['notebooks']
)
IGNORE = ["DC_Mise-a-la-masse", "DC_inversion_2D_example"]

class TestNotebooks(unittest.TestCase):

    def test_notebooks(self):
        Test = testipynb.TestNotebooks(directory=NBDIR, timeout=1800)
        self.assertTrue(Test.run_tests())

if __name__ == "__main__":
    unittest.main()
