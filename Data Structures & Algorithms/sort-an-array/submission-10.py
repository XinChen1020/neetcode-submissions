import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # quick sort

        def partition(arr, l, r):
            pivot_idx = random.randint(l, r)
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]
            pivot = nums[r]

            i = l

            for j in range(l, r):
                if arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1

            arr[r], arr[i] = arr[i], arr[r]

            return i
        
        def quick_sort(arr, l, r):
            if l < r:
                pivot = partition(arr, l, r)
                quick_sort(arr, l, pivot - 1)
                quick_sort(arr, pivot + 1, r)
        
        quick_sort(nums, 0, len(nums) - 1)

        return nums
