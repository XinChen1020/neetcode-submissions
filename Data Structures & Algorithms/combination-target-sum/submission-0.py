class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        stack = deque([(0, 0, [])])
        while stack:
            curr_idx, curr_sum, last_result = stack.pop()
            if curr_sum == target:
                result.append(last_result)
            for i in range(curr_idx, len(nums)):
                if curr_sum + nums[i] <= target:
                    stack.append((i, curr_sum + nums[i], last_result + [nums[i]]))
        return result