"""
Open directory 'Selenium4-Raghvedra-2021' in terminal and execute the following command:
---------------------------------------------------------------------
python -m unittest tests.test__example_8_1_unittest__basic_asserts -v
---------------------------------------------------------------------
or discover and execute all the tests with the command:
-------------------------------
python -m unittest discover -v
-------------------------------
"""
import unittest


class TestCase1(unittest.TestCase):
    def test1(self):
        s1 = "Python"
        s2 = "Java"
        # Verify two strings
        self.assertTrue(s1 == s2, f"'{s1}' and '{s2}' do not match")

