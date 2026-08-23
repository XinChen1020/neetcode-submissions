import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(l, r):
            # Must use random pivot to avoid worst case on 
            # nearly sorted array
            pivot_idx = random.randint(l, r)
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
            pivot = nums[r]

            # slow fast pointer
            # everything before i is smaller than pivot
            # j go through the array
            i = l
            for j in range(l, r):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            # place pivot to correct position
            nums[i], nums[r] = nums[r], nums[i]

            return i
        
        def qucikSort(l, r):
            if l < r:
                pivot = partition(l, r)

                # Left
                qucikSort(l, pivot - 1)

                # Right
                qucikSort(pivot + 1, r)
        
        qucikSort(0, len(nums) - 1)
        
        return nums       


