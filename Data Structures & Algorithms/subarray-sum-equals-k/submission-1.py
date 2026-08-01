class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:


        # prefix sum 

        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[i - 1])
        
        seen_counter = Counter()
        seen_counter[0] += 1
        result = 0
        for i in range(len(prefix_sum)):
            if prefix_sum[i] - k in seen_counter:
                result += seen_counter[prefix_sum[i] - k]
            seen_counter[prefix_sum[i]] += 1
        
        return result
