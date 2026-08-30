class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Binary search
        # How to reduce chunk
        # Conditions
        # mid could be on left ( nums[mid] >= nums[0] and nums[0] >= nums[-1]) or right (n)
        # if mid is on the left chunk
        # 1) if target if lower 

        l, r = 0, len(nums) - 1

        while l <= r:
            
            mid = (r - l) // 2 + l

            if nums[mid] == target:
                return True
            
            if nums[mid] < nums[r]:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            elif nums[mid] > nums[r]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # due to the duplicate, 
                # if nums[mid] == nums[r], we can only safly back r by 1
                r -= 1

        return False