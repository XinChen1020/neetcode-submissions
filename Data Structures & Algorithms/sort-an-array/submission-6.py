class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Merge sort
        def merge(arr, l, mid, r):
            left, right = arr[l:mid + 1], arr[mid + 1: r + 1]

            # i -> original array 
            # j -> left 
            # k -> right
            i, j , k = l, 0, 0

            # write the elements back in order
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            
            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1

            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1


        def mergeSort(arr, l, r):
            if l == r:
                return arr
            mid = (r - l) // 2 + l
            # Two sorted pointer
            mergeSort(arr, l, mid)
            mergeSort(arr, mid + 1, r)
            merge(arr, l, mid, r)

        mergeSort(nums, 0, len(nums) - 1)

        return nums