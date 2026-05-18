class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for idx, n in enumerate(numbers):

            if n in seen:
                return [seen[n] + 1, idx + 1]
            else:
                dif = target - n
                seen[dif] = idx
