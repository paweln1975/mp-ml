import unittest
from unittest.mock import patch
from lists import combine_and_sort_lists
from tuples import create_tuple, create_tuple_from_user_input
from dicts import create_dict_from_user_input
from sets import combine_sets, update_set

class TestLists(unittest.TestCase):
    def test_combine_and_sort_lists(self):
        list1 = [3, 1]
        list2 = [5, 2]
        list3 = [4]
        result = combine_and_sort_lists(list1, list2, list3)
        self.assertEqual(result, [1, 2, 3, 4, 5])


class TestTuples(unittest.TestCase):
    def test_tuple_creation(self):
        name = "Test"
        data = [1, 2, 3]
        result = create_tuple(name, data)
        self.assertEqual(result, ("Test", 1, 2, 3))

    def test_tuple_creation_correct_type(self):
        name = "Example"
        data = [4, 5, 6]
        result = create_tuple(name, data)
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 4)

    def test_create_tuple_from_user_input(self):
        # Mocking input for testing purposes
        with patch('builtins.input', return_value='7, 8, 9'):
            result = create_tuple_from_user_input()
            self.assertEqual(result, (7, 8, 9))

        # Testing with empty input
        with patch('builtins.input', return_value=''):
            result = create_tuple_from_user_input()
            self.assertEqual(result, ())

class TestDicts(unittest.TestCase):
    def test_create_dict_from_user_input(self):
        # Mocking input for testing purposes
        with patch('builtins.input', return_value='key1:1, key2:2'):
            result = create_dict_from_user_input()
            self.assertEqual(result, {'key1': 1, 'key2': 2})

        # Testing with empty input
        with patch('builtins.input', return_value=''):
            result = create_dict_from_user_input()
            self.assertEqual(result, {})

class TestSets(unittest.TestCase):
    def test_set_combination(self):
        # Example set creation
        example_set_1 = {20, 40, 60, 80, 100}
        example_set_2 = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
        set_3 = combine_sets(example_set_1, example_set_2)
        self.assertIsInstance(set_3, set)
        self.assertEqual(len(set_3), 10)

    def test_set_update(self):
        # Example set creation
        example_set_1 = {20, 40, 60, 80, 100}
        example_set_2 = {10, 30, 50, 70, 80, 90, 100}
        updated_set = update_set(example_set_1, example_set_2)
        self.assertIsInstance(updated_set, set)
        self.assertEqual(len(updated_set), 10)

if __name__ == "__main__":
    unittest.main()