class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        dp_1 = 1
        dp_2 = 1
        result = 1

        for i in range(1, len(arr)):

            if ((i % 2 == 0 and arr[i - 1] < arr[i]) or
                (i % 2 != 0 and arr[i - 1] > arr[i])):
                dp_1 += 1
            else:
                dp_1 = 1

            if ((i % 2 == 0 and arr[i - 1] > arr[i]) or
                (i % 2 != 0 and arr[i - 1] < arr[i])):
                dp_2 += 1
            else:
                dp_2 = 1

            result = max(result, dp_1, dp_2)

        return result