class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)

        if k == 0:
            return

        # flip the array
        nums.reverse()

        # Flip 0:k
        nums[:k] = nums[:k][::-1]

        # flip k:
        nums[k:] = nums[k:][::-1]

