class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(start, nums):

            nonlocal result
            if start == len(nums):
                result.append(nums.copy())
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                dfs(start + 1, nums)
                nums[start], nums[i] = nums[i], nums[start]
                
        dfs(0, nums)
        return result