import unittest


class HappyNumberDetector:
    
    def is_happy(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 4:
            return False
        
        next_sum = self._get_next_sum(n)
        return self.is_happy(next_sum)
  
    def _get_next_sum(self, number: int) -> int:
        total_sum = 0
        while number > 0:
            digit = number % 10    
            total_sum += digit * digit   
            number //= 10   
        return total_sum


 
class UnitTests(unittest.TestCase):
    
    def setUp(self):
        """Runs before every test case to initialize the detector."""
        self.detector = HappyNumberDetector()

    def test_happy_numbers(self):
        """Test known happy numbers that should return True."""
        self.assertTrue(self.detector.is_happy(19))   
        self.assertTrue(self.detector.is_happy(7))    
        self.assertTrue(self.detector.is_happy(1))   

    def test_unhappy_numbers(self):
        """Test known unhappy numbers that enter a cycle and should return False."""
        self.assertFalse(self.detector.is_happy(2))    
        self.assertFalse(self.detector.is_happy(4))  
        self.assertFalse(self.detector.is_happy(22))  

    def test_large_happy_number(self):
        """Test a larger happy number."""
        self.assertTrue(self.detector.is_happy(1111111))  

if __name__ == '__main__':
    unittest.main()