import unittest

class SortEngine: 
 
    def sort(self, array): 
        if len(array) <= 1: 
            return array         
            
        mid = len(array) // 2 
         
        left = array[:mid] 
        right = array[mid:] 
         
        left = self.sort(left) 
        right = self.sort(right) 
         
        return self._merge(left, right) 
 
    def _merge(self, left, right): 
        result = [] 
        i = 0 
        j = 0 
         
        while i < len(left) and j < len(right): 
            if left[i] <= right[j]: 
                result.append(left[i]) 
                i += 1 
            else: 
                result.append(right[j]) 
                j += 1 
                 
        while i < len(left): 
            result.append(left[i]) 
            i += 1             
        while j < len(right): 
            result.append(right[j]) 
            j += 1 
             
        return result  


class UnitTests(unittest.TestCase):

    def setUp(self):
        """Provides a fresh instance of the sorting engine before each test."""
        self.engine = SortEngine()

    def test_basic_unsorted(self):
        """Standard case: A completely unsorted list should be ordered correctly."""
        unsorted_list = [5, 2, 9, 1, 5, 6]
        result = self.engine.sort(unsorted_list)
        self.assertEqual(result, [1, 2, 5, 5, 6, 9])

    def test_empty_list(self):
        """Edge case: Sorting an empty list should safely return an empty list."""
        self.assertEqual(self.engine.sort([]), [])

    def test_single_element(self):
        """Edge case: A list with one item should remain unchanged."""
        self.assertEqual(self.engine.sort([42]), [42])

    def test_already_sorted(self):
        """Efficiency check: An already sorted list should return identical output."""
        sorted_list = [1, 2, 3, 4, 5]
        self.assertEqual(self.engine.sort(sorted_list), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        """Worst-case scenario: A list in strict descending order should be inverted."""
        reverse_list = [10, 8, 6, 4, 2]
        self.assertEqual(self.engine.sort(reverse_list), [2, 4, 6, 8, 10])

    def test_negative_numbers(self):
        """Data types: Should perfectly sort a mixture of negative and positive integers."""
        mixed_list = [3, -1, 0, -5, 2]
        self.assertEqual(self.engine.sort(mixed_list), [-5, -1, 0, 2, 3])
 
 
if __name__ == "__main__":
    unittest.main()