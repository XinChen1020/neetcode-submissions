from functools import cache
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        # Alice's max amount
        @cache
        def dfs(i , a_turn):
            if i >= len(stoneValue):
                return 0

            if a_turn:
                score = float("-inf")
                for j in range(i + 1, i + 4):
                    score = max(score, sum(stoneValue[i:j]) + dfs(j, False))
            else:
                score = float("inf")
                for j in range(i + 1, i + 4):
                    score = min(score, dfs(j, True))
            
            return score
        a_result = dfs(0, True)

        if sum(stoneValue) - a_result > a_result:
            return "Bob"
        elif sum(stoneValue) - a_result < a_result:
            return "Alice"
        else:
            return "Tie"