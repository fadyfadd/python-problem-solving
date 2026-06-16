from collections import Counter
import heapq
import unittest

class TopKFrequencyFinder:
    def get_top_k_frequent_elements(self, nums: list[int], k: int) -> list[int]:
 
        if not nums or k == 0:
            return []
 
        element_counts = Counter(nums)
 
        min_heap = []
        for element, count in element_counts.items():
            heapq.heappush(min_heap, (count, element))
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
 
        return [element for count, element in min_heap]


 
class UnitTests(unittest.TestCase):
    def setUp(self):
        self.finder = TopKFrequencyFinder()

    def test_standard_case(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        result = self.finder.get_top_k_frequent_elements(nums, k)
        self.assertEqual(sorted(result), [1, 2])

    def test_single_element(self):
        nums = [1]
        k = 1
        result = self.finder.get_top_k_frequent_elements(nums, k)
        self.assertEqual(result, [1])

    def test_k_equals_total_unique_elements(self):
        nums = [4, 4, 5, 5, 6, 6]
        k = 3
        result = self.finder.get_top_k_frequent_elements(nums, k)
        self.assertEqual(sorted(result), [4, 5, 6])

    def test_empty_input(self):
        nums = []
        k = 5
        result = self.finder.get_top_k_frequent_elements(nums, k)
        self.assertEqual(result, [])

    def test_k_is_zero(self):
        nums = [1, 2, 3]
        k = 0
        result = self.finder.get_top_k_frequent_elements(nums, k)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()