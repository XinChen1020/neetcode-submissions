from functools import cache
class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        @cache
        def get(idx):
            return mountainArr.get(idx)

        # Find mid point
        l, r = 1, mountainArr.length() - 2

        while l <= r:
            mid = (r - l) // 2 + l

            prev = get(mid - 1)
            peak = get(mid)
            after = get(mid + 1)

            if prev < peak and peak > after:
                peak = mid
                break
            
            if prev < peak < after:
                l = mid + 1
            else:
                r = mid - 1
        

        l, r = 0, peak
        while l <= r:
            mid = (r - l) // 2 + l
            
            curr = get(mid)

            if curr == target:
                return mid
            
            if curr > target:
                r = mid - 1
            else:
                l = mid + 1

        l, r = peak + 1, mountainArr.length() - 1
        while l <= r:
            mid = (r - l) // 2 + l
            
            curr = get(mid)

            if curr == target:
                return mid
            
            if curr > target:
                l = mid + 1
            else:
                r = mid - 1

        
        return -1