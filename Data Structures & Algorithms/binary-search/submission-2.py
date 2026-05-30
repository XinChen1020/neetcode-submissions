class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n_len = len(nums)
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r - l) // 2 + l
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1