class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search

        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (r - l) // 2 + l

            if nums[mid] == target:
                return mid

            # left part is sorted
            if nums[mid] >= nums[l]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # right part is sorted
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
           

        return -1