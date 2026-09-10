from functools import cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        @cache
        def dfs(l, r, alice_turn):
            if l > r:
                return 0

            if alice_turn:
                return max(
                    piles[l] + dfs(l + 1, r, False),
                    piles[r] + dfs(l, r - 1, False)
                )
            else:
                return min(
                    dfs(l + 1, r, True),
                    dfs(l, r - 1, True)
                )

        alice = dfs(0, len(piles) - 1, True)
        bob = sum(piles) - alice

        return alice > bob