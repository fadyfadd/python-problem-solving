import unittest


class PacificAtlanticWaterFlow:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []
            
        M = len(heights)
        N = len(heights[0])
        winners = []
        
        for r in range(M):
            for c in range(N):
                visited = [[False] * N for _ in range(M)]
                final_status = self._dfs(r, c, heights, visited, M, N)
                
                if "p" in final_status and "a" in final_status:
                    winners.append([r, c])
                    
        return winners

    def _dfs(self, r: int, c: int, heights: list[list[int]], visited: list[list[bool]], M: int, N: int) -> str:
        visited[r][c] = True
        
        status = ""
        if r == 0 or c == 0:
            status += "p"
        if r == M - 1 or c == N - 1:
            status += "a"
            
        if "p" in status and "a" in status:
            return status
            
        row_offsets = [1, -1, 0, 0]
        col_offsets = [0, 0, 1, -1]
        
        for i in range(4):
            next_r = r + row_offsets[i]
            next_c = c + col_offsets[i]
            
            if 0 <= next_r < M and 0 <= next_c < N:
                if not visited[next_r][next_c]:
                     if heights[next_r][next_c] <= heights[r][c]:
                        child_status = self._dfs(next_r, next_c, heights, visited, M, N)
                        status += child_status
                        
                        if "p" in status and "a" in status:
                            return status
                            
        return status   


 
 
class UnitTests(unittest.TestCase):
    def setUp(self):
        self.sol = PacificAtlanticWaterFlow()

    def test_standard_grid(self):
        """Test a classic multi-row, multi-column grid with varied heights."""
        heights = [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4]
        ]
        expected = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
        
        result = self.sol.pacificAtlantic(heights)       
        self.assertEqual(sorted(result), sorted(expected))

    def test_single_cell(self):
        heights = [[10]]
        expected = [[0, 0]]
        self.assertEqual(self.sol.pacificAtlantic(heights), expected)