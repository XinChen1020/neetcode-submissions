class Solution:
    def jump(self, nums: List[int]) -> int:
        
        l = r = 0
        step = 0
        while r < len(nums) - 1:
            farthest = r
            for i in range(l, r + 1):
                farthest = max(farthest, min(nums[i] + i, len(nums)))
            
            l = r
            r = farthest

            step += 1
        
        return step