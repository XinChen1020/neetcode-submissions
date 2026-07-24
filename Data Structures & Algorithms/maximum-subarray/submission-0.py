class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = float("-inf")
        current_max = float("-inf")
        for n in nums:
            current_max = max(n, current_max + n)
            result = max(result, current_max)
        return result
