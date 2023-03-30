"""
Open directory 'Selenium4-Raghvedra-2021' in terminal and execute the following command:
--------------------------------------------------------------------
python -m unittest tests.test__example_12_2_unittest__collections -v
--------------------------------------------------------------------

or discover and execute all the found tests with the command:
------------------------------
python -m unittest discover -v
------------------------------
"""
import unittest


def setUpModule():
    """ Called once, before executing the module """
    pass

def tearDownModule():
    """ Called once, after executing the module """
    pass


class TestCase3(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ Called once, before all test methods in this class """
        cls.list1 = ["Python", "Selenium"]
        cls.list2 = ["Selenium", "Python"]
        cls.tuple1 = ("Python", "Selenium")
        cls.tuple2 = ("Selenium", "Python")
        cls.set1 = {"Python", "Selenium"}
        cls.set2 = {"Selenium", "Python"}
        cls.dict1 = {"key1": "value1", "key2": "value2"}
        cls.dict2 = {"key2": "value2", "key1": "value1"}

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

    def test15(self):
        self.assertListEqual(self.list1, self.list2, "some text if the test fails")

    def test16(self):
        self.assertTupleEqual(self.tuple1, self.tuple2, "some text if the test fails")

    def test17(self):
        self.assertSetEqual(self.set1, self.set2, "some text if the test fails")

    def test18(self):
        self.assertDictEqual(self.dict1, self.dict2, "some text if the test fails")

    def test19(self):
        self.assertIn("Py", "Python", "some text if the test fails")

    def test20(self):
        self.assertNotIn("Py", "Python", "some text if the test fails")

# test15 (tests.test__example_12_2_unittest__collections.TestCase3) ... FAIL
# test16 (tests.test__example_12_2_unittest__collections.TestCase3) ... FAIL
# test17 (tests.test__example_12_2_unittest__collections.TestCase3) ... ok
# test18 (tests.test__example_12_2_unittest__collections.TestCase3) ... ok
# test19 (tests.test__example_12_2_unittest__collections.TestCase3) ... ok
# test20 (tests.test__example_12_2_unittest__collections.TestCase3) ... FAIL
# ...
