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
        
        for i in range(len(nums)):
            # Go backward since d[j] depends on previous cell
            # Early stop since if nums[i] > j, we always skip -> remain the same
            for j in range(target, nums[i] - 1, -1):
                dp[j] = dp[j] or dp[j - nums[i]]

        return dp[-1]
                