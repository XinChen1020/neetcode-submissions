class Solution:
    def trap(self, height: List[int]) -> int:
        prefix_max = [0] * len(height)
        suffix_max = [0] * len(height)

        prefix_max[0] = height[0]
        for i in range(1, len(height)):
            prefix_max[i] = max(prefix_max[i-1], height[i - 1])
        
        suffix_max[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i+1], height[i + 1])


        result = 0
        for i in range(1, len(height) - 1):
            short = min(prefix_max[i], suffix_max[i])
            if short > height[i]:
                result += short - height[i]
        return result