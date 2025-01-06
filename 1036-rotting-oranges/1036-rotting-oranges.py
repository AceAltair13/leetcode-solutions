class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rotten = set()
        fresh = set()
        current_queue = deque()
        hour = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    current_queue.append((i, j))
        
        if not fresh:
            return 0

        while current_queue:
            next_queue = deque()
            while current_queue:
                x, y = current_queue.popleft()

                for dx, dy in directions:
                    X = x + dx
                    Y = y + dy
                    if (
                        X < n and X >= 0 and
                        Y < m and Y >= 0 and
                        (X, Y) in fresh
                    ):
                        fresh.remove((X, Y))
                        next_queue.append((X, Y))
                    
            if next_queue:
                hour += 1
                current_queue = next_queue
                
        return -1 if fresh else hour