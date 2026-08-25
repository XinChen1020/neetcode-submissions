import random
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # sort 
        # quick sort
        def partition(arr, l, r):
            # Random select pivot to avoid worst case
            pivot_index = random.randint(l, r)
            arr[pivot_index], arr[r] = arr[r], arr[pivot_index]
            pivot = arr[r]
            # Two pointer
            # i -> keep track of 
            i = l

            for j in range(l, r):
                if arr[j] < pivot:
                    arr[i], arr[j] = arr[j], arr[i]
                    i += 1
            arr[i], arr[r] = arr[r], arr[i]

            return i
        
        def quick_sort(arr, l, r):
            if l < r:
                pivot = partition(arr, l, r)
                quick_sort(arr, l, pivot - 1)
                quick_sort(arr, pivot + 1, r)
        
        quick_sort(nums, 0, len(nums) - 1)



