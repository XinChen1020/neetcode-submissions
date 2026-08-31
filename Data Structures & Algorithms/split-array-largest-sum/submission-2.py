from functools import cache
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # backtracking
        # Try out all ways to do k split
        # record the minimal largest sum
        n = len(nums)
        result = float("inf")

        @cache
        def dfs(i, remain_split) -> int | float:

            if i == len(nums) and remain_split == 0:
                return 0
            if i == len(nums) and remain_split > 0:
                return float("inf")
            if remain_split == 0:
                return float('inf')
            
            # n - remain_split because the max we can get 
            # for current split is i to n - remain_split
            # since we need to leave at least remain_split for 
            # other splits (each take up at least 1)
            res = float("inf")
            curr_sum = 0
            for j in range(i, n - remain_split + 1):
                curr_sum += nums[j]
                res = min(res, max(curr_sum, dfs(j + 1, remain_split- 1)))
                if curr_sum > res:
                    break
            return res
        return dfs(0, k)