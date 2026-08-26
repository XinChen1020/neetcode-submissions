class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROW, COL = len(matrix), len(matrix[0])

        # Use an additional row and column of 0 as padding
        # Hence, prefix[i][j] = sum at matrix[i - 1][j - 1]
        self.prefix = [[0] * (COL + 1) for _ in range(ROW + 1)]

        for i in range(1, ROW + 1):
            row_sum = 0
            for j in range(1, COL + 1):
                row_sum += matrix[i - 1][j - 1]
                self.prefix[i][j] = self.prefix[i - 1][j] + row_sum

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        return self.prefix[row2][col2] - self.prefix[row1 - 1][col2] - self.prefix[row2][col1 - 1] + self.prefix[row1 - 1][col1 - 1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)