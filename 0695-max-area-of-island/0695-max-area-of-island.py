class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        def bfs(i, j):
            q = collections.deque()
            visited.add((i, j))
            q.append((i, j))
            area = 0
            
            while q:
                x, y = q.popleft()
                area += 1
                for dx, dy in directions:
                    X = x + dx
                    Y = y + dy
                    if (
                        X in range(ROWS) and
                        Y in range(COLS) and
                        (X, Y) not in visited and
                        grid[X][Y] == 1
                    ):
                        q.append((X, Y))
                        visited.add((X, Y))
            
            return area
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(max_area, bfs(i, j))
        
        return max_area


            