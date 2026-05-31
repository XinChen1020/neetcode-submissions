class Solution:
    def findMin(self, nums: List[int]) -> int:

        l,r = 0, len(nums) - 1
        while l < r:
            mid = (r - l) // 2 + l
            if nums[r] > nums[mid]:
                r = mid
            else:
                l = mid + 1
        
        return nums[r]
        