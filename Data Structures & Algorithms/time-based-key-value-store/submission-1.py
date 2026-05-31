from collections import defaultdict, deque
class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(dict)
        self.time_map_deque = defaultdict(deque)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key][timestamp] = value
        self.time_map_deque[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        target_deque = self.time_map_deque[key]
        if len(target_deque) == 0:
            return ""

        l, r = 0, len(target_deque)
        while l < r:
            mid = (r - l) // 2 + l
            if target_deque[mid] == timestamp:
                return self.time_map[key][target_deque[mid]]
            
            if timestamp < target_deque[mid]:
                r = mid
            else:
                l = mid + 1
        return self.time_map[key][target_deque[l - 1]] if target_deque[l - 1] <= timestamp else ""