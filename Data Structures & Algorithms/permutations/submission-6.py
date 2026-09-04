class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        seen = set()
        def dfs(curr_res):
            nonlocal result
            if len(curr_res) == len(nums):
                result.append(curr_res)
                return
            
            for i in range(len(nums)):
                if i not in seen:
                    seen.add(i)
                    dfs(curr_res + [nums[i]])
                    seen.remove(i)
            
        dfs([])
        return result
