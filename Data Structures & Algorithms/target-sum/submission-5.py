class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Bottom up DP version
        # dp[i][j] = ways to get target j using nums[i:]
        # For each i , either + or -
        # dp[i][j] = dp[i + 1][j - nums[i]] + dp[i + 1][j + nums[i]]
        # Use defaultdict instead of array for each row due to negative target
        # Base case: dp[len(nums)][0] = 1
        # Space optimized since each i only depends on i + 1

        prev = defaultdict(int)
        prev[0] = 1

        for i in range(len(nums) - 1, -1, -1):
            curr = defaultdict(int)
            for amount, count in prev.items():
                curr[amount + nums[i]] += count
                curr[amount - nums[i]] += count
            prev = curr
        

        return curr[target]