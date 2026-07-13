class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Bottom up DP version
        # dp[i][j] = ways to get target j using nums[i:]
        # For each i , either + or -
        # dp[i][j] = dp[i + 1][j - nums[i]] + dp[i + 1][j + nums[i]]
        # Use defaultdict instead of array for each row due to negative target
        # Base case: dp[i][j] = 1 when i == j

        dp = [defaultdict(int) for _ in range(len(nums) + 1)]

        dp[len(nums)][0] = 1

        for i in range(len(nums) - 1, -1, -1):
            for amount, count in dp[i + 1].items():
                dp[i][amount + nums[i]] += count
                dp[i][amount - nums[i]] += count


        return dp[0][target]