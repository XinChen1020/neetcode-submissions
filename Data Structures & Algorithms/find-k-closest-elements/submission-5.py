class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # binary search
        # Must be continous array
        # Use binary search to find the starting index
        # if the array is too right:
        # distance from the arr[m] is less than distance from arr[m + k]
        # if the array too left:
        
        l, r = 0, len(arr) - k - 1
        # open
        while l <= r:
            mid = (r - l) // 2 + l

            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid - 1
        
        return arr[l:l + k]
