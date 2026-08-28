class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Boyer-Moore Voting
        # elements with less than n/3 would be eliminated at the end
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

            if len(count) <= 2:
                continue

            new_count = defaultdict(int)
            for k, v in count.items():
                count[k] -= 1
                if count[k] > 0:
                    new_count[k] = count[k]
                
            count = new_count
        result = []
        for k, v in count.items():
            if nums.count(k) > len(nums) // 3:
                result.append(k)
        return result