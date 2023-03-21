"""
Open directory 'Selenium4-Raghvedra-2021' in terminal and execute the following command:
------------------------------------------------------------------------------------
python -m unittest tests.test__example_8_1_unittest__basic_and_comparison_asserts -v
------------------------------------------------------------------------------------
or discover and execute all the tests with the command:
-------------------------------
python -m unittest discover -v
-------------------------------
"""
import unittest


class TestCaseBasicAsserts(unittest.TestCase):
    def setUp(self):
        self.s1 = "Python"
        self.s2 = "Java"
        self.v1 = None

    def test01(self):
        self.assertTrue(self.s1 == self.s2, f"'{self.s1}' and '{self.s2}' do not match")

    def test02(self):
        self.assertFalse(self.s1 == self.s2, f"'{self.s1}' and '{self.s2}' match")

    def test03(self):
        self.assertIs(None, [], "some text if the test fails")

    def test04(self):
        self.assertIsNot((), [], "some text if the test fails")

    def test05(self):
        self.assertIsNone(self.v1, "some text if the test fails")

    def test06(self):
        self.assertIsNotNone(self.v1, "some text if the test fails")

    def test07(self):
        self.assertIsInstance(self.s1, str, "some text if the test fails")

    def test08(self):
        self.assertNotIsInstance(self.v1, str, "some text if the test fails")


class TestCaseComparisonAsserts(unittest.TestCase):
    def test09(self):
        self.assertEqual(1, 2, "some text if the test fails")

    def test10(self):
        self.assertNotEqual(1, 2, "some text if the test fails")

    def test11(self):
        self.assertGreater("b", "a", "some text if the test fails")

    def test12(self):
        self.assertGreaterEqual("aa", "a", "some text if the test fails")

    def test13(self):
        self.assertLess("b", "a", "some text if the test fails")

    def test14(self):
        self.assertLessEqual("aa", "a", "some text if the test fails")

# test01 (tests.test__example_8_1_unittest__basic_and_comparison_asserts.TestCaseBasicAsserts) ... FAIL
# test02 (tests.test__example_8_1_unittest__basic_and_comparison_asserts.TestCaseBasicAsserts) ... ok
# test03 (tests.test__example_8_1_unittest__basic_and_comparison_asserts.TestCaseBasicAsserts) ... FAIL
# test04 (tests.test__example_8_1_unittest__basic_and_comparison_asserts.TestCaseBasicAsserts) ... ok
# test05 (tests.test__example_8_1_unittest__basic_and_comparison_asserts.TestCaseBasicAsserts) ... ok
# test06 (tests.test__example_8_1_unittest__basic_and_comparison_asserts.TestCaseBasicAsserts) ... FAIL
# test07 (tests.test__example_8_1_unittest__basic_and_comparison_asserts.TestCaseBasicAsserts) ... ok
# test08 (tests.test__example_8_1_unittest__basic_and_comparison_asserts.TestCaseBasicAsserts) ... ok
# test09 (tests.test__example_8_1_unittest__basic_and_comparison_asserts.TestCaseComparisonAsserts) ... FAIL
# test10 (tests.test__example_8_1_unittest__basic_and_comparison_asserts.TestCaseComparisonAsserts) ... ok
# test11 (tests.test__example_8_1_unittest__basic_and_comparison_asserts.TestCaseComparisonAsserts) ... ok
# test12 (tests.test__example_8_1_unittest__basic_and_comparison_asserts.TestCaseComparisonAsserts) ... ok
# test13 (tests.test__example_8_1_unittest__basic_and_comparison_asserts.TestCaseComparisonAsserts) ... FAIL
# test14 (tests.test__example_8_1_unittest__basic_and_comparison_asserts.TestCaseComparisonAsserts) ... FAIL
#
# ======================================================================
# FAIL: test01 (tests.test__example_8_1_unittest__basic_and_comparison_asserts.TestCaseBasicAsserts)
# ----------------------------------------------------------------------
# ...
