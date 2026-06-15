import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def partition(l, r):
            # randomly choose pivot, then move it to the end
            pivot_idx = random.randint(l, r)
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]

            pivot = l

            for idx in range(l, r):
                if nums[idx] > nums[r]:
                    nums[pivot], nums[idx] = nums[idx], nums[pivot]
                    pivot += 1

            nums[r], nums[pivot] = nums[pivot], nums[r]
            return pivot
        
        l, r = 0, len(nums) - 1
        target = k - 1

        while True:
            pivot = partition(l, r)

            if pivot == target:
                return nums[pivot]
            elif pivot > target:
                r = pivot - 1
            else:
                l = pivot + 1