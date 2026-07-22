from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Bottom up version dp
        # dp[i][j] = max coin you get using nums[l:r]
        # last one to pop
        new_nums = [1] + nums + [1]

        dp = [[0] * (len(nums) + 2) for _ in range(len(nums) + 2)]
        for l in range(len(nums), 0, -1):
            for r in range(l, len(nums) + 1):
                for i in range(l, r + 1):
                    coins = new_nums[l - 1] * new_nums[i] * new_nums[r + 1]
                    coins += dp[l][i - 1] + dp[i + 1][r]
                    dp[l][r] = max(dp[l][r], coins)
                
        # dp was made and defined based on new nums
        # so we don't want dp[0][-1]
        return dp[1][len(nums)]
