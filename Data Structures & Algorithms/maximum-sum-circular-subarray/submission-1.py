class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Kadne's algo
        # either keep current number or start a new subarry 

        curr_max = 0
        max_result = float("-inf")

        curr_min = 0
        min_result = float("inf")

        total = 0

        for n in nums:
            curr_max = max(n, curr_max + n)
            max_result = max(max_result, curr_max)
            total += n
            curr_min = min(n, curr_min + n)
            min_result = min(min_result, curr_min)



        return max(max_result, total - min_result) if max_result > 0 else max_result