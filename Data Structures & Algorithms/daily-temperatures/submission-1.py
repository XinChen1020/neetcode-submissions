class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono_stack = deque()
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while mono_stack and temperatures[i] > mono_stack[-1][0]:
                temp, idx = mono_stack.pop()
                result[idx] = i - idx
            mono_stack.append((temperatures[i], i))
        
        # Clear remaining stack
        while mono_stack:
            temp, idx = mono_stack.pop()
            result[idx] = 0

        return result