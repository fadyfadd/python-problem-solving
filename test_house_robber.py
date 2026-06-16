 
import unittest

# Assuming your class is defined here
class HouseRobber:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 2)
        for i in range(n):
            dp[i + 2] = max(dp[i + 1], nums[i] + dp[i])
        return dp[n + 1]


class UnitTests(unittest.TestCase):
    def setUp(self):
        self.hr = HouseRobber()

    def test_standard_case(self):
        """Test with your classic example [2, 7, 9, 3, 1] -> Expected: 12 (2 + 9 + 1)"""
        self.assertEqual(self.hr.rob([2, 7, 9, 3, 1]), 12)

    def test_alternating_adjacent(self):
        """Test where robbing adjacent houses looks tempting but skipping is better [1, 2, 3, 1] -> Expected: 4 (1 + 3)"""
        self.assertEqual(self.hr.rob([1, 2, 3, 1]), 4)

    def test_single_house(self):
        """Edge Case: Only one house on the street."""
        self.assertEqual(self.hr.rob([5]), 5)

    def test_two_houses(self):
        """Edge Case: Two houses, should pick the one with maximum value."""
        self.assertEqual(self.hr.rob([4, 9]), 9)

    def test_empty_street(self):
        """Edge Case: No houses to rob."""
        self.assertEqual(self.hr.rob([]), 0)

    def test_all_zeros(self):
        """Edge Case: Houses exist but contain no money."""
        self.assertEqual(self.hr.rob([0, 0, 0, 0]), 0)

    def test_large_gap(self):
        """Test where skipping two houses in a row is optimal to hit a massive jackpot [2, 1, 1, 10] -> Expected: 12 (2 + 10)"""
        self.assertEqual(self.hr.rob([2, 1, 1, 10]), 12)

if __name__ == '__main__':
    unittest.main()