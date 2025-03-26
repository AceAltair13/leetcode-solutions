class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # TC: O(M x N)
        # SC: O(1)

        M = len(matrix)
        N = len(matrix[0])

        first_row_is_zero = any(matrix[0][j] == 0 for j in range(N))
        first_col_is_zero = any(matrix[i][0] == 0 for i in range(M))

        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        for i in range(1, M):
            for j in range(1, N):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_is_zero:
            for j in range(N):
                matrix[0][j] = 0
        
        if first_col_is_zero:
            for i in range(M):
                matrix[i][0] = 0
        
        