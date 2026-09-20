class Solution:
    def trap(self, height: List[int]) -> int:
        # Logic:
        # The volume of water at each position is determined
        # by the min(max height on the left of it, max height on the right of it)
        # use left_max, right_max to keep track of max height seen so far
        # move the pointer on the side that has the lower max height inward
        # since we know that the max height on that side is lower
        # than whatever on the other side (there might be higher on but it doesn't
        # matter since the water volume depends on the lower max height and the height of the other side is at least higher than that side's current seen max height)
        # For equal heights, it doesn't matter

        left_max, right_max = height[0], height[-1]

        l, r = 0, len(height) - 1

        result = 0

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                result += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                result += right_max - height[r]

        return result


