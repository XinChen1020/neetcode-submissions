class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        total = 0
        n = len(digits)
        for i in range(n):
            total += digits[n - i - 1] * (10 ** i)
        
        total += 1
        result = []
        while total > 0:
            result.append(total % 10)
            total //= 10 

        result.reverse()
        return result