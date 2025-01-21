class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = Counter(tuple(row) for row in grid)
        n = len(grid)
        ans = 0

        for c in range(n):
            col = tuple(grid[r][c] for r in range(n))
            if col in rows:
                ans += rows[col]
        
        return ans

        