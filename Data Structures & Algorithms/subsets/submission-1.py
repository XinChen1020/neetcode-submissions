class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n_len = len(nums)

        # (current index, previous result)
        stack = deque([(0, [])])

        while stack:
            idx, curr_result = stack.pop()

            # reached end of the nums
            if idx == n_len:
                result.append(curr_result)
                continue
            
            # include current num
            stack.append((idx + 1, curr_result + [nums[idx]]))

            # exclude current num
            stack.append((idx + 1, curr_result))

        return result
