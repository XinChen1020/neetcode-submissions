class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy
        # Determine the closet and furthest you can get in 1, 2, 3,.... steps
        # When the furthest reach over the the end, you got your minimal steps
        # Similar to BFS
        # O(n)
        result = 0 
        l = r = 0

        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            result += 1

        return result