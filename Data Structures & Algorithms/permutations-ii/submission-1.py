class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        curr = []
        used = [False] * len(nums)

        def dfs():
            if len(curr) == len(nums):
                result.append(curr[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                # Don't use the same value twice at this recursion level
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                curr.append(nums[i])

                dfs()

                curr.pop()
                used[i] = False

        dfs()
        return result