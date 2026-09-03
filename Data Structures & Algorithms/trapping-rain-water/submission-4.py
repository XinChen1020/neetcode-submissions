class Solution:
    def trap(self, height: List[int]) -> int:
        
        left_max, right_max = height[0], height[-1]
        l, r = 0, len(height) - 1
        total = 0

        while l < r:
            if left_max > right_max:
                r -= 1

                if height[r] > right_max:
                    right_max = height[r]
                else:
                    total += right_max - height[r]
                
            else:
                l += 1

                if height[l] > left_max:
                    left_max = height[l]
                else:
                    total += left_max - height[l]
                
        return total