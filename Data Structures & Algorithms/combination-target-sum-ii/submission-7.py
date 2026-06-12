class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        # idx -> next index to begin searching for candidates
        # curr_sum -> current sum 
        # curr -> result
        def dfs(idx, curr_sum, curr_result):
            if curr_sum == target:
                result.append(curr_result)
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if curr_sum + candidates[i] > target:
                    break

                dfs(i + 1, curr_sum + candidates[i], curr_result + [candidates[i]])
        
        dfs(0, 0, [])
        return result
        