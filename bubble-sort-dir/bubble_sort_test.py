import unittest # import unittest framework
from bubble_sort import bubble_sort # import bubble_sort function from bubble_sort file

class testBubbleSort(unittest.TestCase): # create class which inherits attributes and methods from the class testCase in the unittest framework

    def test_bubble_sort_with_positive_numbers(self):
        self.assertEqual(bubble_sort([5, 5, 7, 8, 2, 4, 1]), [1, 2, 4, 5, 5, 7, 8]) # checks if the bubble_sort function can sort positive numbers correctly 

    def test_bubble_sort_empty_list(self):
        self.assertEqual(bubble_sort([]), []) # verifies that the result of sorting an empty list is an empty list



if __name__ == '__main__':
    unittest.main(verbosity=2) # unittest.main provides a command-line interface to test the script, verbosity is just a way to describe how much info will display
