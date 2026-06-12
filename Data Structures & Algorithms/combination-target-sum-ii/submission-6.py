from collections import Counter, deque
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        items = sorted(Counter(candidates).items())  # [(num, count)]
        res = []

        stack = deque([(0, target, [])])

        while stack:
            idx, remaining, path = stack.pop()

            if remaining == 0:
                res.append(path)
                continue

            if idx == len(items):
                continue

            # Option 1: skip current number
            stack.append((idx + 1, remaining, path))

            # Option 2: take current number 1..count times
            num, count = items[idx]
            max_take = min(count, remaining // num)

            for k in range(1, max_take + 1):
                stack.append((idx + 1, remaining - k * num, path + [num] * k))

        return res