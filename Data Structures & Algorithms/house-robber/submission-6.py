class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_1, rob_2 = 0, 0

        for n in nums:
            temp = rob_2
            rob_2 = max(rob_2, n + rob_1)
            rob_1 = temp
        
        return rob_2