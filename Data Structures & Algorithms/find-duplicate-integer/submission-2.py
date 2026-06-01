class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]

        # Phase 1: find meeting point inside the cycle
        while fast != slow:
            slow = nums[slow]
            fast = nums[nums[fast]]

        # Phase 2: find entrance of cycle
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
        
