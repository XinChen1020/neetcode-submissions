class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        result = float("inf")

        l = 0
        current_total = 0
        for r in range(len(nums)):
            current_total += nums[r]

            while l <= r and current_total >= target:
                result = min(result, r - l + 1)

                current_total -= nums[l]
                l += 1

        return result if result != float("inf") else 0