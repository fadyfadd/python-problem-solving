import unittest

class PathFinder:
    def unique_paths(self, m: int, n: int) -> int:
        if m <= 0 or n <= 0:
            return 0
        if m == 1 or n == 1:
            return 1
            
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            dp[i][0] = 1
            
        for j in range(n):
            dp[0][j] = 1
            
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                
        return dp[m - 1][n - 1]

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.finder = PathFinder()

    def test_standard_grid(self):
        self.assertEqual(self.finder.unique_paths(3, 7), 28)
        self.assertEqual(self.finder.unique_paths(3, 2), 3)

    def test_single_row_or_column(self):
        self.assertEqual(self.finder.unique_paths(1, 1), 1)
        self.assertEqual(self.finder.unique_paths(1, 5), 1)
        self.assertEqual(self.finder.unique_paths(5, 1), 1)

    def test_invalid_dimensions(self):
        self.assertEqual(self.finder.unique_paths(0, 5), 0)
        self.assertEqual(self.finder.unique_paths(5, -1), 0)

if __name__ == '__main__':
    unittest.main()