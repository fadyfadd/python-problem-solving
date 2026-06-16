from collections import Counter
import unittest
 
class StringUtils:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        required_counts = Counter(t)
        required_unique = len(required_counts)
        
        window_counts = {}
        formed_unique = 0
        
       
        ans = (float("inf"), None, None)
        
        trailing = 0
        for leading in range(len(s)):
            char = s[leading]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            if char in required_counts and window_counts[char] == required_counts[char]:
                formed_unique += 1
                
 
            while formed_unique == required_unique:
                current_len = leading - trailing + 1
                if current_len < ans[0]:
                    ans = (current_len, trailing, leading)
                    
                left_char = s[trailing]
                window_counts[left_char] -= 1
                
                if left_char in required_counts and window_counts[left_char] < required_counts[left_char]:
                    formed_unique -= 1
                    
                trailing += 1
                
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1] 

 
class UnitTests(unittest.TestCase):
    
    def setUp(self):
        """Runs before every single test method to provide a fresh instance."""
        self.sol = StringUtils()

    def test_basic(self):
        """Standard case: Should find the minimum window 'BANC'"""
        self.assertEqual(self.sol.minWindow("ADOBECODEBANC", "ABC"), "BANC")

    def test_exact_match(self):
        """Exact match: Should return the whole string if s matches t perfectly"""
        self.assertEqual(self.sol.minWindow("a", "a"), "a")

    def test_no_match(self):
        """No match: Should return an empty string if t's letters aren't in s"""
        self.assertEqual(self.sol.minWindow("abcd", "z"), "")

    def test_duplicate_requirements(self):
        """Duplicates: Should handle when t requires multiples of the same letter"""
        self.assertEqual(self.sol.minWindow("AABECODEBANC", "AA"), "AA")

    def test_empty_inputs(self):
        """Edge case: Empty strings should not crash the code"""
        self.assertEqual(self.sol.minWindow("", "ABC"), "")
        self.assertEqual(self.sol.minWindow("ABC", ""), "")
 
if __name__ == "__main__":
    unittest.main()