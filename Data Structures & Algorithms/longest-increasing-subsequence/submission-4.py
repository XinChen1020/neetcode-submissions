from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        @cache
        def dfs(j):
            # LIS ending exactly at index j
            LIS = 1

            for i in range(j):
                if nums[i] < nums[j]:
                    LIS = max(LIS, dfs(i) + 1)

            return LIS

        return max(dfs(j) for j in range(len(nums)))