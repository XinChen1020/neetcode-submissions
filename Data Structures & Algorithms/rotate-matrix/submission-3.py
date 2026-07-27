class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Transpose
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Invert
        #matrix.reverse()

        for i in range(n):
            for j in range(0, n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
