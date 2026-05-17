class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_sum = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix_sum[i] = nums[i-1] * prefix_sum[i-1]
        
        suffix_sum = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suffix_sum[i] = nums[i+1] * suffix_sum[i+1]

        result = []
        for i in range(len(nums)):
            result.append(prefix_sum[i] * suffix_sum[i])
        return result