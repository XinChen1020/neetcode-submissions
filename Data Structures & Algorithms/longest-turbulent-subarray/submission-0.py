class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        if len(arr) == 1:
            return 1

        result = 1

        dp = [[1] * len(arr) for _ in range(2)]


        for i in range(1, len(arr)):
            
            # first pattern
            if (i % 2 == 0 and arr[i - 1] < arr[i]) or \
            (i % 2 != 0 and arr[i - 1] > arr[i]):
                dp[0][i] = dp[0][i - 1] + 1
                result = max(result, dp[0][i])
            
            if (i % 2 == 0 and arr[i - 1] > arr[i]) or \
            (i % 2 != 0 and arr[i - 1] < arr[i]):
                dp[1][i] = dp[1][i - 1] + 1
                result = max(result, dp[1][i])
            
        return result


