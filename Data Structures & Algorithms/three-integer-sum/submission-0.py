class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        for i in range(len(nums) - 2):
            seen = {}
            target = -nums[i]
            # two sum

            for j in range(i + 1, len(nums)):

                if nums[j] in seen:
                    result.add(tuple(sorted([nums[i], nums[j], nums[seen[nums[j]]]])))

                seen[target - nums[j]] = j
        return [list(r) for r in result]