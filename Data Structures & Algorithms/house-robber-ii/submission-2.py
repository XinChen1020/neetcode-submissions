class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # Two array
        rob_1, rob_2 = 0, 0

        for n in nums[:-1]:
            temp = rob_2
            rob_2 = max(rob_1 + n, rob_2)
            rob_1 = temp
        result_1 = rob_2

        rob_1, rob_2 = 0, 0

        for n in nums[1:]:
            temp = rob_2
            rob_2 = max(rob_1 + n, rob_2)
            rob_1 = temp

        result_2 = rob_2

        return max(result_1, result_2)