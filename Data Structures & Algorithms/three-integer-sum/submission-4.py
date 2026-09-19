class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)

        for i in range(n - 2):

            # Skip duplicate first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]

            j = i + 1
            k = n - 1

            while j < k:
                total = nums[j] + nums[k]

                if total == target:
                    result.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    # Skip duplicate j values
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicate k values
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif total > target:
                    k -= 1
                    
                    # Skip duplicate k values
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                else:
                    j += 1

                    # Skip duplicate j values
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return result