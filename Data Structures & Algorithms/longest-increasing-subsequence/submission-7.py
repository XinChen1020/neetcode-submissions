class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # dp[i] is the longest increasing sequence that ends at 
        # nums[i]

        dp = [1] * len(nums)
        dp[0] = 1
        result = 1

        for j in range(len(nums)):
            for i in range(j):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i] + 1)
            result = max(result, dp[j])
        return result
