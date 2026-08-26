class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pre_sum = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        # Initialize first row and first column
        cum_total = 0
        for j in range(len(matrix[0])):
            cum_total += matrix[0][j]
            self.pre_sum[0][j] = cum_total
        cum_total = 0
        for i in range(len(matrix)):
            cum_total += matrix[i][0]
            self.pre_sum[i][0] = cum_total

        # Get square sum
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                self.pre_sum[i][j] = matrix[i][j] + self.pre_sum[i - 1][j] + self.pre_sum[i][j - 1] - self.pre_sum[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        result = self.pre_sum[row2][col2]

        if row1 - 1 >= 0:
            result -= self.pre_sum[row1 - 1][col2]
        
        if col1 - 1 >= 0:
            result -= self.pre_sum[row2][col1 - 1]
        
        if row1 - 1 >= 0 and col1 - 1 >= 0:
            result += self.pre_sum[row1 - 1][col1 - 1]
        return result

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)