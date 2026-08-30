class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        result = 0
        for n in hashset:
            if n - 1 not in hashset:
                curr = n
                curr_len = 0
                while curr in hashset:
                    curr_len += 1
                    curr += 1
                    result = max(curr_len, result)
        
        return result