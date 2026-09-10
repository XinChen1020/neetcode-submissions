from functools import cache
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        
        # Alice's advantage
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
                    score = min(score, -sum(stoneValue[i:j]) + dfs(j, True))
            
            return score
        a_advantage = dfs(0, True)

        if a_advantage < 0:
            return "Bob"
        elif a_advantage > 0:
            return "Alice"
        else:
            return "Tie"