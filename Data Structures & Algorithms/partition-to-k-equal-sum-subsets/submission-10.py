class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # The other way
        # let the decision be which group to put the current number into

                # If total can't be partitioned into equal parts
        if sum(nums) % k != 0:
            return False
        
        target = sum(nums) // k
        groups = [0] * k
        used = set()
        nums.sort(reverse = True)

        def dfs(i):
            
            if i == len(nums):
                return True
            
            for g in range(len(groups)):
                if groups[g] + nums[i] > target:
                    continue
                groups[g] += nums[i]
                if dfs(i + 1):
                    return True
                groups[g] -= nums[i]

                if groups[g] == 0:
                    break
            
            return False
        
        return dfs(0)
                