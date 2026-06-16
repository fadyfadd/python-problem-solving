 

import unittest

# Paste the Solution class here
class DistanceUtils:
    def editDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
            
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
        return dp[m][n]


class UnitTests(unittest.TestCase):
    def setUp(self):
        self.sol = DistanceUtils()

    def test_standard_cases(self):
        
        self.assertEqual(self.sol.editDistance("horse", "ros"), 3)        
        self.assertEqual(self.sol.editDistance("intention", "execution"), 5)

    def test_empty_strings(self):       
        self.assertEqual(self.sol.editDistance("", ""), 0)
        self.assertEqual(self.sol.editDistance("abc", ""), 3)
        self.assertEqual(self.sol.editDistance("", "abc"), 3)

    def test_identical_strings(self):
        self.assertEqual(self.sol.editDistance("abcde", "abcde"), 0)

    def test_completely_different(self):
        self.assertEqual(self.sol.editDistance("abc", "xyz"), 3)

    def test_single_character(self):
        self.assertEqual(self.sol.editDistance("a", "b"), 1)
        self.assertEqual(self.sol.editDistance("a", "a"), 0)


if __name__ == "__main__":
    unittest.main()