import unittest

class ArrayEvaluator:
    def remove_duplicate(self, nums: list[int]) -> int:
        """
        Removes duplicates from a sorted array in-place.
        Returns the number of unique elements.
        """
        if not nums:
            return 0
            
        unique_index = 0
        for search_index in range(1, len(nums)):
            if nums[search_index] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[search_index]
                
        return unique_index + 1


 
class UnitTests(unittest.TestCase):
    def setUp(self):
        self.evaluator = ArrayEvaluator()

    def test_empty_array(self):
        nums = []
        result = self.evaluator.remove_duplicate(nums)
        self.assertEqual(result, 0)
        self.assertEqual(nums, [])

    def test_no_duplicates(self):
        nums = [1, 2, 3, 4, 5]
        result = self.evaluator.remove_duplicate(nums)
        self.assertEqual(result, 5)
        self.assertEqual(nums[:result], [1, 2, 3, 4, 5])

    def test_all_duplicates(self):
        nums = [2, 2, 2, 2, 2]
        result = self.evaluator.remove_duplicate(nums)
        self.assertEqual(result, 1)
        self.assertEqual(nums[:result], [2])

    def test_mixed_duplicates(self):
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        result = self.evaluator.remove_duplicate(nums)
        self.assertEqual(result, 5)
        self.assertEqual(nums[:result], [0, 1, 2, 3, 4])

    def test_negative_numbers(self):
        nums = [-3, -3, -1, 0, 0, 2]
        result = self.evaluator.remove_duplicate(nums)
        self.assertEqual(result, 4)
        self.assertEqual(nums[:result], [-3, -1, 0, 2])


if __name__ == "__main__":
    unittest.main()