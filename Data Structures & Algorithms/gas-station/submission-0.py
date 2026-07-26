class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If total cost more than total gas, no way to complete anyway
        # other wise there must be an solution
        if sum(gas) < sum(cost):
            return -1

        total = 0
        start = 0
        # Only start point with gas > cost is able to start
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                start = i + 1

        return start