class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[-1]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        if len(dp) <= 2:
            return max(dp[0], dp[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        
        return dp[-1]
