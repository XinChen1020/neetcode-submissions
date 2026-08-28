class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Prefix sum + Two sum 
        # prefix_sum[i] = sum of nums[0:i]
        prefix_sum = [0] * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        
        result = 0
        prev = defaultdict(int)
        for i in range(len(nums) + 1):
            result += prev[prefix_sum[i] - k]
            prev[prefix_sum[i]] += 1

        return result
