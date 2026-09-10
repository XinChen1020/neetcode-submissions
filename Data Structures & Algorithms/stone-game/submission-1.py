from functools import cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        @cache
        def dfs(l, r):
            if l > r:
                return 0

            result = 0
            if piles[l] > piles[r]:
                result += piles[l]

            else:
                result += piles[r]
            
            result += dfs(l + 1, r - 1)

            return result

            
        a = dfs(0, len(piles) - 1)
        return sum(piles) - a < a

