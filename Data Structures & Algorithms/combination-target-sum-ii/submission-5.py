class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
       
        result = []
        freq_available = Counter(candidates)
        candidates = sorted(freq_available.keys())

        stack = deque([[0, 0, []]])

        while stack:
            curr_idx, curr_sum, last_result = stack.pop()

            if curr_sum == target:
                result.append(last_result)
                continue

            for i in range(curr_idx, len(candidates)):
                for j in range(1, freq_available[candidates[i]] + 1):
                    if curr_sum + j * candidates[i] > target:
                        break
                    stack.append([i + 1, curr_sum + j * candidates[i], last_result + j * [candidates[i]]])

        return result


