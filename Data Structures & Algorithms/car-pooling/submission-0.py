class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # can't take more than capacity at any time
        # Line sweep?
        events = []
        for p, start, end in trips:
            events.append((start, p))
            events.append((end, -p))
        
        events.sort()
        active = 0
        for t, p in events:
            active += p 
            if active > capacity:
                return False
        
        return True