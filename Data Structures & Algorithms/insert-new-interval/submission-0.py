class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        result = []
        overlap = newInterval
        idx = 0
        # Front
        while idx < len(intervals) and \
        intervals[idx][0] < newInterval[0] and \
        intervals[idx][1] < newInterval[0]:
            result.append(intervals[idx])
            idx += 1
        
        # Overlap
        overlap = newInterval
        while idx < len(intervals) and \
        not (intervals[idx][0] > overlap[1] and \
        intervals[idx][1] > overlap[1]):
        
            overlap = [min(intervals[idx][0], overlap[0]), max(intervals[idx][1], overlap[1])]
            idx += 1
        
        result.append(overlap)

        result += intervals[idx:]
        
        return result