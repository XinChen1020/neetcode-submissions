class Solution:
    def climbStairs(self, n: int) -> int:
        pre_1, pre_2 = 1, 1
        
        for i in range(n - 1):
            temp = pre_1
            pre_1 = pre_1 + pre_2
            pre_2 = temp
        
        return pre_1
