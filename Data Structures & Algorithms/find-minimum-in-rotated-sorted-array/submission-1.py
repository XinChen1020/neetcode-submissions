class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        l,r = 0, len(nums)
        n_len = len(nums)
        while l < r:
            mid = (r - l) // 2 + l

            if nums[(mid + 1) % n_len] > nums[mid] and nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[r - 1] > nums[l]:
                r = mid
            elif nums[mid] > nums[l]:
                l = mid + 1
            else:
                r = mid
        
        return l
        