"""
Open directory 'Selenium4-Raghvedra-2021' in terminal and execute one of the following commands:
----------------------------------------------------------------
python -m unittest -v tests.test__example_12_1_unittest__basics
python3 -m unittest -v tests.test__example_12_1_unittest__basics
----------------------------------------------------------------

or discover and execute all the found tests with the commands:
-------------------------------
python -m unittest discover -v
python3 -m unittest discover -v
-------------------------------

Alternatively, add the following code to run the tests of the module:
------------------------------
if __name__ == "__main__":
    unittest.main(verbosity=2)
------------------------------
and run the script as usual:
----------------------------------------------------
python tests.test__example_12_1_unittest__basics.py
python3 tests.test__example_12_1_unittest__basics.py
----------------------------------------------------

See more information about unit test here:
https://docs.python.org/3/library/unittest.html
"""
import unittest


def setUpModule():
    """ Called once, before executing the module """
    print("In tests.test__example_12_1_unittest__basics, in setUpModule")

def tearDownModule():
    """ Called once, after executing the module """
    print("In tests.test__example_12_1_unittest__basics, in tearDownModule")


class TestCase1(unittest.TestCase):
    """ Short description of test case class """
    @classmethod
    def setUpClass(cls):
        """ Called once, before all test methods in this class """
        print("In TestCase1, in setUpClass")
        cls.s1 = "Python"
        cls.s2 = "Java"
        cls.v1 = None

    @classmethod
    def tearDownClass(cls):
        """ Called once, after all test methods in this class, if setUpClass was successful """
        print("In TestCase1, in tearDownClass")

    def setUp(self):
        """ Called multiple times, before every test method in this class """
        print("\nIn TestCase1, in setUp")

    def tearDown(self):
        """ Called multiple times, after every test method in this class """
        print("In TestCase1, in tearDown")

    def test01(self):
        """ Short description of test method """
        print(f"In {self.id()}")
        print(f"Description: {self.shortDescription()}")
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


class TestCase2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ Called once, before all test methods in this class """
        pass

    @classmethod
    def tearDownClass(cls):
        """ Called once, after all test methods in this class, if setUpClass was successful """
        pass

    def setUp(self):
        """ Called multiple times, before every test method in this class """
        pass

    def tearDown(self):
        """ Called multiple times, after every test method in this class """
        pass

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


# In tests.test__example_12_1_unittest__basics, in setUpModule
# In TestCase1, in setUpClass
# test01 (tests.test__example_12_1_unittest__basics.TestCase1)
# Short description of test method ...
# In TestCase1, in setUp
# In tests.test__example_12_1_unittest__basics.TestCase1.test01
# Description: Short description of test method
# In TestCase1, in tearDown
# FAIL
# test02 (tests.test__example_12_1_unittest__basics.TestCase1) ...
# In TestCase1, in setUp
# In TestCase1, in tearDown
# ok
# test03 (tests.test__example_12_1_unittest__basics.TestCase1) ...
# In TestCase1, in setUp
# In TestCase1, in tearDown
# FAIL
# test04 (tests.test__example_12_1_unittest__basics.TestCase1) ...
# In TestCase1, in setUp
# In TestCase1, in tearDown
# ok
# test05 (tests.test__example_12_1_unittest__basics.TestCase1) ...
# In TestCase1, in setUp
# In TestCase1, in tearDown
# ok
# test06 (tests.test__example_12_1_unittest__basics.TestCase1) ...
# In TestCase1, in setUp
# In TestCase1, in tearDown
# FAIL
# test07 (tests.test__example_12_1_unittest__basics.TestCase1) ...
# In TestCase1, in setUp
# In TestCase1, in tearDown
# ok
# test08 (tests.test__example_12_1_unittest__basics.TestCase1) ...
# In TestCase1, in setUp
# In TestCase1, in tearDown
# ok
# In TestCase1, in tearDownClass
# test09 (tests.test__example_12_1_unittest__basics.TestCase2) ... FAIL
# test10 (tests.test__example_12_1_unittest__basics.TestCase2) ... ok
# test11 (tests.test__example_12_1_unittest__basics.TestCase2) ... ok
# test12 (tests.test__example_12_1_unittest__basics.TestCase2) ... ok
# test13 (tests.test__example_12_1_unittest__basics.TestCase2) ... FAIL
# test14 (tests.test__example_12_1_unittest__basics.TestCase2) ... FAIL
# In tests.test__example_12_1_unittest__basics, in tearDownModule
# ...
