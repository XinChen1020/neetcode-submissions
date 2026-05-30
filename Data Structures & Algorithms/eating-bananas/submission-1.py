
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # l is min case (k = 1)
        # r is max case (k = max(piles) since max is one pile at a time)
        l,r = 1, max(piles) + 1

        while l < r:
            mid = (r - l) // 2 + l

            total_time = sum([math.ceil(p / mid) for p in piles])
            
            # if k = mid consume > h time, that means it need to eat faster
            # Hence, move the left pointer
            if total_time > h:
                l = mid + 1
            else:
                r = mid
        
        return l
