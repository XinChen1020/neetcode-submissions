class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Bottom Up dp -> 0/1 backpack
        # Space optimized
        total_sum = sum(nums)
        target = total_sum // 2
        # odd total can't be split into subset with integer only
        if total_sum % 2 != 0:
            return False
        # dp[i] -> whether we can form sum j using frist i numbers
        dp = [False] * (target + 1)

        # Base case
        dp[0] = True
        
        for i in range(1, len(nums) + 1):
            # Go backward since d[j] depends on previous cell
            for j in range(target, 0, -1):

                if j >= nums[i - 1]:
                    # Skip or take nums[i]
                    dp[j] = dp[j] or dp[j - nums[i-1]]
                else:
                    # If nums[i - 1] is larger than the sum j, we can only skip it
                    dp[j] = dp[j]
        return dp[-1]
                