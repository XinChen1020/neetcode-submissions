"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        
        # Keep filling the room greedy
        prev_ends = []
        room = 0
        for i in range(len(intervals)):
            need_room = True
            for j in range(len(prev_ends)):
                if intervals[i].start >= prev_ends[j]:
                    need_room = False
                    prev_ends[j] = intervals[i].end
                    break

            if need_room:
                room += 1
                prev_ends.append(intervals[i].end)
        return room