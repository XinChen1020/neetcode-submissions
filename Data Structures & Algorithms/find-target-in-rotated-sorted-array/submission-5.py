class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            mid = (r - l) // 2 + l
            print(l, r)
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid
            else:
                # mid on the other segment
                if target < nums[mid] or target > nums[r - 1]:
                    r = mid
                else:
                    l = mid + 1
        return -1