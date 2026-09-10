class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)

        if target % 2 != 0:
            return False
        
        target = target // 2

        # dp[i][j] = can we get remaining j within nums[i:]
        prev = [False] * (target + 1)

        prev[0] = True

        for i in range(len(nums) - 1, -1, -1):
            dp = [False] * (target + 1)
            dp[0] = True
            
            for j in range(target + 1):
                
                dp[j] = prev[j] 

                if j - nums[i] >= 0:
                    dp[j] |= prev[j - nums[i]]
                
            prev = dp

        return dp[target]
        
        