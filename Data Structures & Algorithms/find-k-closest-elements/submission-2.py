class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Two pointer
        l, r = 0, len(arr) - 1

        while r - l + 1 > k:
            # Keep moving the pointer that points to the furthest one
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            elif abs(arr[l] - x) < abs(arr[r] - x):
                r -= 1
            else:
                # If both equal, l will the closet since r is always > l
                r -= 1
        
        return arr[l:r + 1]