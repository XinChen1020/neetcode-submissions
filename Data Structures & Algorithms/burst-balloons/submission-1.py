from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Top down dp
        # DFS with memorization
        # last one to pop
        nums = [1] + nums + [1]

        @cache
        def dfs(l, r):

            if l > r:
                return 0
            
            result = 0
            for i in range(l, r + 1):

                # if ballon i is the last one to burst,
                # this means that everything else outside of i and between [l, r]
                # were bursted. So we take l-1 and r + 1
                coin = nums[l - 1] * nums[i] * nums[r + 1]
                
                # Now we can track the best on left and right before
                # poping this ballon
                coin += dfs(l, i - 1) + dfs(i + 1, r)
                result = max(result, coin)
            return result
            
        
        return dfs(1, len(nums) - 2)