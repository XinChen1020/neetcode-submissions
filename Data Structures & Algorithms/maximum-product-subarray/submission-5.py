class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Kadane's algorithm
        # either start an new array using current number, or continue multiple
        # previous product with current number, which ever is larger
        if len(nums) == 1:
            return nums[0]
        curr_max = nums[0]
        curr_min = nums[0]

        result = float("-inf")
        for i in range(1, len(nums)):
            temp = curr_max
            curr_max = max(nums[i], nums[i] * curr_max, nums[i] * curr_min)
            curr_min = min(nums[i], nums[i] * temp, nums[i] * curr_min)

            result = max(result, curr_max)
        
        return result