class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # more than n/3 time
        # there could only be 0, 1 , 2 result.
        # If 3, each would have a max of n/3 element, not more
        return [n for n, c in Counter(nums).most_common(2) if c > len(nums) / 3]

        


        