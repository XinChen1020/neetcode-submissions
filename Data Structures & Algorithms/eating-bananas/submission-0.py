
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        

        l,r = 1, max(piles) + 1

        while l < r:
            mid = (r - l) // 2 + l

            total_time = sum([math.ceil(p / mid) for p in piles])

            if total_time > h:
                l = mid + 1
            else:
                r = mid
        
        return l
