import unittest


class NumberOfIslands:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0
        
        island_count = 0
        rows = len(grid)
        cols = len(grid[0])
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island_count += 1
                    self._dfs(grid, r, c)
                    
        return island_count

    def _dfs(self, grid: list[list[str]], r: int, c: int) -> None:
        rows = len(grid)
        cols = len(grid[0])
        
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        
 
        grid[r][c] = '0'
        
        self._dfs(grid, r + 1, c)  # Down
        self._dfs(grid, r - 1, c)  # Up
        self._dfs(grid, r, c + 1)  # Right
        self._dfs(grid, r, c - 1)  # Left



class UnitTests(unittest.TestCase):
    def setUp(self):
        self.solver = NumberOfIslands()

    def test_empty_grid(self):
        """Should return 0 for an empty grid."""
        grid = []
        self.assertEqual(self.solver.numIslands(grid), 0)

    def test_all_water(self):
        """Should return 0 when there is no land."""
        grid = [
            ['0', '0', '0'],
            ['0', '0', '0'],
            ['0', '0', '0']
        ]
        self.assertEqual(self.solver.numIslands(grid), 0)

    def test_single_island_fills_grid(self):
        """Should return 1 when the entire grid is one island."""
        grid = [
            ['1', '1'],
            ['1', '1']
        ]
        self.assertEqual(self.solver.numIslands(grid), 1)

    def test_multiple_islands_standard(self):
        """Standard LeetCode case with multiple distinct islands."""
        grid = [
            ['1', '1', '0', '0', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '1', '0', '0'],
            ['0', '0', '0', '1', '1']
        ]
        # Island 1: Top-left 2x2
        # Island 2: Middle single cell
        # Island 3: Bottom-right 1x2
        self.assertEqual(self.solver.numIslands(grid), 3)

    def test_diagonal_islands_do_not_connect(self):
        """Diagonals should not connect; these should be treated as 2 separate islands."""
        grid = [
            ['1', '0'],
            ['0', '1']
        ]
        self.assertEqual(self.solver.numIslands(grid), 2)

    def test_single_cell_island(self):
        """Should correctly identify a single isolated land piece."""
        grid = [['1']]
        self.assertEqual(self.solver.numIslands(grid), 1)

if __name__ == '__main__':
    unittest.main()