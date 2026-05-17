class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_exist = set(nums)
        max_len = 0
        for n in num_exist:
            if n - 1 not in num_exist:
                curr_len = 0
                curr_num = n
                while curr_num in num_exist:
                    curr_len += 1
                    curr_num += 1
                max_len = max(max_len, curr_len)
        return max_len
        

        