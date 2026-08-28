class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Linear time
        # constant space
        # 0 isn't positive 
        # Only care about positve really since negative don't matter to
        # result selection

        # We could use a hashset -> O(n) space though
        # Ways to store the scan result
        
        # result must be in the range of 1 to len(nums) + 1
        # Use original nums as extra space:
        # If nums[i] is negative, result = i + 1 exist in the input array
        
        n_len = len(nums)

        # Remove negative number since they don't affect the result
        for i in range(n_len):
            if nums[i] < 0:
                nums[i] = 0
        
        # Mark the input array as the extra space needed:
        for i in range(n_len):
            val = abs(nums[i])
            # Need abs since the number could already be marked as negative
            if 1 <= val <= n_len:
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (n_len + 1)
        print(nums)
        # Check potential results:
        for i in range(1, n_len + 1):
            if nums[i - 1] >= 0:
                return i
        return n_len + 1
