class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Greedy
        # Remove any later overlap interval since we don't want to expand
        # the boundary
        intervals.sort()
        result = 0
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prev_end:
                prev_end = min(intervals[i][1], prev_end)
                result += 1
            else:
                prev_end = intervals[i][1]
        return result