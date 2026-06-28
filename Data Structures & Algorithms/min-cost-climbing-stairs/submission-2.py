class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        pre, current = 0, 0

        for i in range(2, len(cost) + 1):
            temp = current
            current = min(pre + cost[i-2], current + cost[i - 1])
            pre = temp
        
        return current