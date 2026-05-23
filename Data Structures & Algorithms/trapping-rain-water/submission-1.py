class Solution:
    def trap(self, height: List[int]) -> int:
            mono_stack = []
            result = 0

            for i in range(len(height)):

                while mono_stack and height[mono_stack[-1]] < height[i]:
                    
                    top_idx = mono_stack.pop()

                    if not mono_stack:
                        continue

                    prev_greater = height[mono_stack[-1]]
                    next_greater = height[i]

                    result += (min(prev_greater, next_greater) - height[top_idx]) * (i - mono_stack[-1] - 1) 

                mono_stack.append(i)
            return result