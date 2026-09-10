class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)

        if target % 2 != 0:
            return False
        
        target = target // 2

        # dp[i][j] = can we get remaining j within nums[i:]
        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]

        for i in range(len(nums) + 1):
            dp[i][0] = True

        for i in range(len(nums) - 1, -1, -1):
            for j in range(target + 1):
                
                dp[i][j] = dp[i + 1][j] 

                if j - nums[i] >= 0:
                    dp[i][j] |= dp[i + 1][j - nums[i]]
        
        return dp[0][target]
        
        