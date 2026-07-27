"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Improved version with min heap
        # min heap keep the room with the earlist end time

        intervals.sort(key = lambda x: x.start)
        
        # Keep filling the room greedy
        prev_ends = []
        room = 0
        for i in range(len(intervals)):
            if not prev_ends or intervals[i].start < prev_ends[0]:
                room += 1
            else:
                heapq.heappop(prev_ends)
            
            heapq.heappush(prev_ends, intervals[i].end)

            
        return room