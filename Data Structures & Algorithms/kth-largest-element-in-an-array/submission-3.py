class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def partition(l, r):
            # use last element as pivot
            pivot = l

            for idx in range(l, r):
                if nums[idx] < nums[r]:
                    nums[pivot], nums[idx] = nums[idx], nums[pivot]
                    pivot += 1

            nums[r], nums[pivot] = nums[pivot], nums[r]
        
            return pivot
        
        l, r = 0, len(nums) - 1
        pivot = len(nums)
        k = len(nums) - k
        while pivot != k:
            pivot = partition(l, r)
            if pivot > k:
                r = pivot - 1
            else:
                l = pivot + 1
                
        return nums[pivot]