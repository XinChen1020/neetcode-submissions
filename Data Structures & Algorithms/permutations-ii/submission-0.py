class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        result = []
        curr_result = []
        def dfs():

            if len(curr_result) == len(nums):
                result.append(curr_result[:])
                return
            
            picked = set()

            for i in range(len(nums)):
                if i not in seen and nums[i] not in picked:
                    seen.add(i)
                    picked.add(nums[i])

                    curr_result.append(nums[i])
                    dfs()

                    curr_result.pop()
                    seen.remove(i)
        
        dfs()
        return result
