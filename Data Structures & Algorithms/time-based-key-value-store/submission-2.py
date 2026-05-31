from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        target_list = self.time_map[key]
        if not target_list:
            return ""

        l, r = 0, len(target_list)
        while l < r:
            mid = (r - l) // 2 + l
            if target_list[mid][1] == timestamp:
                return self.time_map[key][mid][0]
            
            if timestamp < target_list[mid][1]:
                r = mid
            else:
                l = mid + 1

        return self.time_map[key][l-1][0] if target_list[l - 1][1] <= timestamp else ""