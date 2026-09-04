class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        seen = set()
        curr_res = []

        def dfs():
            if len(curr_res) == len(nums):
                result.append(curr_res[:])  # copy only completed permutation
                return

            for i in range(len(nums)):
                if i not in seen:
                    seen.add(i)
                    curr_res.append(nums[i])

                    dfs()

                    curr_res.pop()
                    seen.remove(i)

        dfs()
        return result