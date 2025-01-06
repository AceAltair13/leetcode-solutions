class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(x, y, i):
            if i == len(word):
                return True
            
            if (
                x < 0 or y < 0 or
                x >= ROWS or y >= COLS or
                word[i] != board[x][y] or 
                (x, y) in path
            ):
                return False

            path.add((x, y))
            res = (
                dfs(x + 1, y, i + 1) or
                dfs(x, y + 1, i + 1) or
                dfs(x - 1, y, i + 1) or
                dfs(x, y - 1, i + 1)
                )
            path.remove((x, y))
            return res
        
        for _i in range(ROWS):
            for _j in range(COLS):
                if dfs(_i, _j, 0):
                    return True
        return False
        
