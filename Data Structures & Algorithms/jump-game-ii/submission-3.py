class Solution:
    def jump(self, nums: List[int]) -> int:
        
        dp = [float("inf")] * len(nums)
        dp[0] = 0

        for i in range(len(nums)):
            
            for j in range(i, min(i + nums[i] + 1, len(nums))):

                dp[j] = min(dp[i] + 1, dp[j])
        return dp[-1]