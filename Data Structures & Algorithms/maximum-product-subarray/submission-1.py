class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp
        # for each n in nums, the max product either continue or get a new start
        # Also need need another to take the negative into account
        if len(nums) == 1:
            return nums[0]
        dp_max = [0] * len(nums)
        dp_min = [0] * len(nums)

        dp_max[0] = nums[0]
        dp_min[0] = nums[0]

        result = float("-inf")
        for i in range(1, len(nums)):
            dp_max[i] = max(nums[i], nums[i] * dp_max[i-1], nums[i] * dp_min[i - 1])
            dp_min[i] = min(nums[i], nums[i] * dp_max[i-1], nums[i] * dp_min[i - 1])

            result = max(result, dp_max[i])
        return result