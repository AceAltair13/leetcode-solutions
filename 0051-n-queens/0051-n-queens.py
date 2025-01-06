class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row, board, columns, diagonals1, diagonals2):
            if row == n:
                # Convert the board configuration to the desired format and store it
                result.append(["".join(r) for r in board])
                return

            for col in range(n):
                if (
                    col in columns
                    or (row - col) in diagonals1
                    or (row + col) in diagonals2
                ):
                    continue  # Skip invalid placements

                # Place the queen
                board[row][col] = "Q"
                columns.add(col)
                diagonals1.add(row - col)
                diagonals2.add(row + col)

                # Recur to the next row
                backtrack(row + 1, board, columns, diagonals1, diagonals2)

                # Remove the queen (backtrack)
                board[row][col] = "."
                columns.remove(col)
                diagonals1.remove(row - col)
                diagonals2.remove(row + col)

        # Initialize
        result = []
        board = [["." for _ in range(n)] for _ in range(n)]
        backtrack(0, board, set(), set(), set())
        return result
