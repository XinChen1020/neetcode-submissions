class Solution:
    def trap(self, height: List[int]) -> int:
            left, right = 1, len(height) - 2
            left_max, right_max = height[0], height[-1]
            result = 0

            while left <= right:
                if left_max > right_max:
                    if height[right] > right_max:
                        right_max = height[right]
                    else:
                        result += right_max - height[right]
                    right -= 1

                else:
                    if height[left] > left_max:
                        left_max = height[left]
                    else:
                        result += left_max - height[left]
                    left += 1

            return result