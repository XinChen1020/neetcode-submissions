class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
       
        result = []
        freq_map = Counter(candidates)
        candidates = sorted(freq_map.keys())

        stack = deque([[0, 0, [], freq_map]])

        while stack:
            curr_idx, curr_sum, last_result, freq_left = stack.pop()

            if curr_sum == target:
                result.append(last_result)
                continue

            for i in range(curr_idx, len(candidates)):
                for j in range(1, freq_left[candidates[i]] + 1):
                    if curr_sum + j * candidates[i] > target:
                        break
                    stack.append([i + 1, curr_sum + j * candidates[i], last_result + j * [candidates[i]], freq_left])

        return result


