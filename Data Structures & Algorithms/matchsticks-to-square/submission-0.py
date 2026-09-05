class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # Can you break matchsticks into 4 subgroups with equal sum
        
        

        # Total must be divisible by 4
        if sum(matchsticks) % 4 != 0:
            return False
        
        # target sum for each group
        target = sum(matchsticks) // 4

        # so we can skip when sum of 1 group is larger than target
        # also prevent duplicate calculation 
        matchsticks.sort()
        used = set()

        def dfs(idx, remaining_group, subset_sum):

            if remaining_group == 0:
                return True
            
            # Find remaining groups
            if subset_sum == target:
                return dfs(0, remaining_group - 1, 0)

            for i in range(idx, len(matchsticks)):
                if i in used or subset_sum + matchsticks[i] > target:
                    continue
                used.add(i)

                # Use current number
                if dfs(i + 1, remaining_group, subset_sum + matchsticks[i]):
                    return True
                used.remove(i)
                
            return False
        return dfs(0, 4, target)

            
