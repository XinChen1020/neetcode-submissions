class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        for i, j in intervals:
            if not result or (i > result[-1][1]):
                result.append([i, j])
            else:
                result[-1] = [min(i, result[-1][0]), max(j, result[-1][1])]
        
        return result
            

        