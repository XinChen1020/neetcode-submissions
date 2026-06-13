class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        stack = deque([[0, []]])

        while stack:
            idx, path = stack.pop()
            
            # No restriction since we want all subsets
            result.append(path)
            
            for i in range(idx, len(nums)):
                
                # Only include the same number once
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                stack.append([i + 1, path + [nums[i]]])

        return result