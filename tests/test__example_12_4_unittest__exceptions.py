"""
Open directory 'Selenium4-Raghvedra-2021' in terminal and execute the following command:
------------------------------------------------------------------------
python -m unittest -v tests.test__example_12_4_unittest__exceptions
------------------------------------------------------------------------

or discover and execute all the found tests with the command:
------------------------------
python -m unittest discover -v
------------------------------
"""
import unittest


def raise_value_error_exception(*args, **kwargs):
    exception_class = ValueError
    print("This function will throw", exception_class.__name__)
    print("args: ", args)
    print("kwargs:", kwargs)
    raise exception_class("some message")


def setUpModule():
    pass


def tearDownModule():
    pass


class TestCase5(unittest.TestCase):
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

    def test27(self):
        """ Check if a method or function throws an exception """
        args = (1, 2, 3)
        kwargs = {"a": "A", "b": "B"}
        self.assertRaises(ValueError, raise_value_error_exception, *args, **kwargs)

# test27 (tests.test__example_12_4_unittest__exceptions.TestCase5)
# Check if a method or function throws an exception ... This function will throw ValueError
# args:  (1, 2, 3)
# kwargs: {'a': 'A', 'b': 'B'}
# ok
# ...
