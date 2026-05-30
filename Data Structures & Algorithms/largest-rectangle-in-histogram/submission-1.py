class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = heights + [0]

        # Next/Prev lower -> increasing stack
        # (height, idx)
        mono_stack = deque()
        result = 0

        for i in range(len(heights)):
            while mono_stack and heights[i] < mono_stack[-1][0]:
                # Add result for each element poped out of the stack
                # which know the prev lower (top of stack) and the next
                # lower (current element)
                h, idx = mono_stack.pop()
                left = mono_stack[-1][1] if mono_stack else -1
                result = max(result, h * (i - left - 1))
            mono_stack.append((heights[i], i))

        return result
        