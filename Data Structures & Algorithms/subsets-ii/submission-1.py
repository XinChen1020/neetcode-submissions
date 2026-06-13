class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)

        # start idx, path so far
        stack = deque([[0, []]])

        while stack:
            idx, path = stack.pop()
            
            if idx == len(nums):
                result.append(path)
                continue
            
            # Keep current number
            stack.append([idx + 1, path + [nums[idx]]])

            # Skip current number
            # To prevent duplicates, also not keeping the path
            # of skipping current and then keep the same number
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            stack.append([idx + 1, path])
        return result 

