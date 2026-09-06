class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        # If total can't be partitioned into equal parts
        if sum(nums) % k != 0:
            return False
        
        target = sum(nums) // k

        used = set()
        nums.sort()

        def dfs(idx, remaining_groups, curr_sum):
            
            # Optimization: since the total is divisible by k 
            # when there's only 1 group left, they must satifiy the restriction
            if remaining_groups == 1:
                return True

            if curr_sum == target:
                return dfs(0, remaining_groups - 1, 0)
            prev = -1
            for i in range(idx, len(nums)):

                if curr_sum + nums[i] > target:
                    break
                # Skip used number or duplicate number
                if i in used or nums[i] == prev:
                    continue
                
                used.add(i)
                if dfs(i + 1, remaining_groups, curr_sum + nums[i]):
                    return True
                used.remove(i)
                prev = nums[i]

                if curr_sum == 0:
                    return False

            return False

        return dfs(0, k, 0)
