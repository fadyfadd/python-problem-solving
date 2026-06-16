import unittest

class DecodeServices:
    def numDecodings(self, s: str) -> int:
 
        if not s or s[0] == '0':
            return 0

        prev2 = 1
        prev1 = 1

        for i in range(1, len(s)):
            current = 0
            single_digit = int(s[i])
            double_digit = int(s[i-1]) * 10 + single_digit
            
 
            if single_digit >= 1:
                current += prev1
 
            if 10 <= double_digit <= 26:
                current += prev2
            
 
            prev2 = prev1
            prev1 = current

        return prev1
    

 
class UnitTests(unittest.TestCase):
    def setUp(self):
        self.sol = DecodeServices()

    def test_base_cases(self):
        """Test simple configurations and valid short strings."""
        self.assertEqual(self.sol.numDecodings("12"), 2)  # 'AB' (1, 2) or 'L' (12)
        self.assertEqual(self.sol.numDecodings("226"), 3) # 'BZ' (2, 26), 'VF' (22, 6), or 'BBF' (2, 2, 6)

    def test_leading_zero(self):
        """Any string starting with '0' cannot be decoded."""
        self.assertEqual(self.sol.numDecodings("0"), 0)
        self.assertEqual(self.sol.numDecodings("06"), 0)

    def test_valid_and_invalid_zeros(self):
        """Test tricky zero placements which force specific groupings."""
        self.assertEqual(self.sol.numDecodings("10"), 1)