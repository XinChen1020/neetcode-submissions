class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # next temp greater than ith -> monotonic stack

        # (index, temp)
        stack = deque()
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                idx, temp = stack.pop()
                result[idx] = i - idx
            
            stack.append((i, temperatures[i]))
            
        return result