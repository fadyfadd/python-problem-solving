import unittest
import array



class ArrayIntersection:
 
    @staticmethod
    def intersect(nums1, nums2):
     
        if len(nums1) > len(nums2):
            return ArrayIntersection.intersect(nums2, nums1)           
   
        my_set = set()
        for num in nums1:
            my_set.add(num)            
        result_list = []
        for num in nums2:
            if num in my_set:
                result_list.append(num)
                my_set.remove(num)               
    
        return array.array('i', result_list) 

 

class UnitTests(unittest.TestCase):

    def test_basic_intersection(self):
        """Standard case: Should find overlapping elements with duplicates handled."""
        n1 = [1, 2, 2, 3]
        n2 = [2, 2, 4]       
        result = list(ArrayIntersection.intersect(n1, n2))
        self.assertEqual(result, [2])

    def test_no_intersection(self):
        """Disjoint arrays: Should return an empty list if there are no common elements."""
        n1 = [1, 2, 3]
        n2 = [4, 5, 6]
        result = list(ArrayIntersection.intersect(n1, n2))
        self.assertEqual(result, [])

    def test_one_empty_array(self):
        """Edge case: One array is completely empty."""
        n1 = []
        n2 = [1, 2, 3]
        result = list(ArrayIntersection.intersect(n1, n2))
        self.assertEqual(result, [])

    def test_all_identical_elements(self):
        """Identical arrays: Intersection should only include unique values once."""
        n1 = [5, 5, 5]
        n2 = [5, 5]
        result = list(ArrayIntersection.intersect(n1, n2))
        self.assertEqual(result, [5])

if __name__ == "__main__":
    unittest.main()