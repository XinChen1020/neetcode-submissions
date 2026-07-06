class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Bottom Up dp -> 0/1 backpack
        total_sum = sum(nums)
        target = total_sum // 2
        # odd total can't be split into subset with integer only
        if total_sum % 2 != 0:
            return False
        # dp[i][j] -> whether we can form sum j using frist i numbers
        dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]

        # Base case
        for i in range(len(nums) + 1):
            dp[i][0] = True
        
        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):

                if j >= nums[i - 1]:
                    # Skip or take nums[i]
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
                else:
                    # If nums[i - 1] is larger than the sum j, we can only skip it
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]
                