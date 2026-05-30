class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Two binary search:
        # one for row, another for column
        l_i, r_i = 0, len(matrix)
        l_j, r_j = 0, len(matrix[0]) 

        # Row binary Search
        while l_i < r_i:
            mid_i = l_i + (r_i - l_i) // 2
            if target >= matrix[mid_i][0] and target <= matrix[mid_i][-1]:
                # Column binary search
                while l_j < r_j:
                    mid_j = l_j + (r_j - l_j) // 2
                    if matrix[mid_i][mid_j] == target:
                        return True
                    elif matrix[mid_i][mid_j] > target:
                        r_j = mid_j
                    else:
                        l_j = mid_j + 1
                return False            
            if target > matrix[mid_i][-1]:
                l_i = mid_i + 1
            elif target < matrix[mid_i][0]:
                r_i = mid_i
            

        return False