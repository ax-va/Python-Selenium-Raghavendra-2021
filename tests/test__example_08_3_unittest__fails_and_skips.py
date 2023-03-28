"""
Open directory 'Selenium4-Raghvedra-2021' in terminal and execute the following command:
------------------------------------------------------------------------
python -m unittest -v tests.test__example_08_3_unittest__fails_and_skips
------------------------------------------------------------------------

or discover and execute all the found tests with the command:
------------------------------
python -m unittest discover -v
------------------------------
"""
import unittest


def setUpModule():
    pass

def tearDownModule():
    pass


class TestCase4(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test21(self):
        """ This test method will be failed """
        self.fail()

    def test22(self):
        """ This test method will be skipped """
        self.skipTest("Some reason why skipped")

    @unittest.skip(reason="Unconditional skip")
    def test23(self):
        """ This test method will be skipped """
        pass

    @unittest.skipIf(condition=True, reason="Conditional skip")  # Condition is set before running setUpClass
    def test24(self):
        """ This test method will be skipped """
        pass

    @unittest.skipUnless(condition=False, reason="Conditional skip")  # Condition is set before running setUpClass
    def test25(self):
        """ This test method will be skipped """
        pass

    @unittest.expectedFailure
    def test26(self):
        """ This test method will not be counted as failed """
        self.assertTrue(False, "False is not True")

# test21 (tests.test__example_08_3_unittest__fails_and_skips.TestCase4)
# This test method will be failed ... FAIL
# test22 (tests.test__example_08_3_unittest__fails_and_skips.TestCase4)
# This test method will be skipped ... skipped 'Some reason why skipped'
# test23 (tests.test__example_08_3_unittest__fails_and_skips.TestCase4)
# This test method will be skipped ... skipped 'Unconditional skip'
# test24 (tests.test__example_08_3_unittest__fails_and_skips.TestCase4)
# This test method will be skipped ... skipped 'Conditional skip'
# test25 (tests.test__example_08_3_unittest__fails_and_skips.TestCase4)
# This test method will be skipped ... skipped 'Conditional skip'
# test26 (tests.test__example_08_3_unittest__fails_and_skips.TestCase4)
# This test method will not be counted as failed ... expected failure
