class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        island_count = 0

        def bfs(i, j):
            q = collections.deque()
            visited.add((i, j))
            q.append((i, j))

            while q:
                a, b = q.popleft()
                directions = [
                    [1, 0],
                    [0, 1],
                    [-1, 0],
                    [0, -1]
                ]

                for dx, dy in directions:
                    ax = a + dx
                    by = b + dy
                    if (
                        ax in range(ROWS) and
                        by in range(COLS) and
                        (ax, by) not in visited and
                        grid[ax][by] == "1"
                    ):
                        visited.add((ax, by))
                        q.append((ax, by))
        
        for i in range(ROWS):
            for j in range(COLS):
                cell = grid[i][j]
                if cell == "1" and (i, j) not in visited:
                    bfs(i, j)
                    island_count += 1

        return island_count