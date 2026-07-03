class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # either start a new sequence or adding on top of previous sequence
        # let dp[i] = longest length subsequence that ends with nums[i]

        dp = [1] * len(nums)
        result = 1
        for j in range(1, len(nums)):
            for i in range(0, j):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i] + 1)
                    result = max(dp[j], result)
        return result