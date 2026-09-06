class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        # If total can't be partitioned into equal parts
        if sum(nums) % k != 0:
            return False
        
        target = sum(nums) // k

        used = set()
        nums.sort()

        def dfs(idx, remaining_groups, curr_sum):

            if remaining_groups == 1:
                return True

            if curr_sum == target:
                return dfs(0, remaining_groups - 1, 0)
            prev = -1
            for i in range(idx, len(nums)):

                if curr_sum + nums[i] > target:
                    break
                if i in used or nums[i] == prev:
                    continue
                
                used.add(i)
                if dfs(i + 1, remaining_groups, curr_sum + nums[i]):
                    return True
                used.remove(i)
                prev = nums[i]

            return False

        return dfs(0, k, 0)
