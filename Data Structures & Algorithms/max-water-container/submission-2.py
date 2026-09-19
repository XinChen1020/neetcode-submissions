class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Two pointer
        # water determine by the lowest bar of two
        # move the lower side
        # since the only possible way to get more water
        # is to find a higher bar inside

        l, r = 0, len(heights) - 1
        result = 0
        while l < r:
            result = max(result, min(heights[l], heights[r]) * (r - l))

            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1

        return result
