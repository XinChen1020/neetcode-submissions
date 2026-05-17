class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # diff : location
        seen = {}
        for idx, n in enumerate(nums):
            if n not in seen:
                seen[target - n] = idx
            else:
                return [seen[n], idx]