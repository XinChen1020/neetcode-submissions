class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l, r = 0, len(intervals) - 1
        intervals.sort()

        # O(log N)
        while l <= r:
            mid = (r - l) // 2 + l
            
            # Find the leftmost interval such that intervals[l][0] >= newInterval[0]
            if intervals[mid][0] >= newInterval[0]:
                r = mid - 1
            else:
                l = mid + 1
        intervals = intervals[:l] + [newInterval] + intervals[l:]

        result = [intervals[0]]

        for i in range(1, len(intervals)):
            
            # Overlap -> Merge
            if intervals[i][0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])
        
        return result
