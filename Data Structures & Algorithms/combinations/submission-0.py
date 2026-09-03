class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # backtracking
        result = []
        def dfs(idx, curr_result):
            nonlocal result
            if idx == n + 1:
                if len(curr_result) == k:
                    result.append(curr_result)
                return
            
            # Include current number
            dfs(idx + 1, curr_result + [idx])

            # Skip
            dfs(idx + 1, curr_result)
        
        dfs(1, [])

        return result

            
