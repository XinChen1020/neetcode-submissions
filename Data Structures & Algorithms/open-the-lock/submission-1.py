class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # do like a graph
        # BFS
        # each level is the number of turns
        # THere's 8 sub tree for each result

        
        queue = deque(["0000"])
        seen = set("0000")
        if "0000" in deadends:
            return -1
        level = 0

        while queue:

            for _ in range(len(queue)):
                curr_comb = queue.popleft()
                if curr_comb == target:
                    return level

                # Forward
                for i in range(4):
                    new_letter = str((int(curr_comb[i]) + 1) % 10)
                    new_comb = curr_comb[:i] + new_letter + curr_comb[i + 1:]
                    if new_comb in deadends or new_comb in seen:
                        continue
                    queue.append(new_comb)
                    seen.add(new_comb)

                # Backward
                for i in range(4):
                    new_letter = str((int(curr_comb[i]) - 1) % 10)
                    new_comb = curr_comb[:i] + new_letter + curr_comb[i + 1:]
                    if new_comb in deadends or new_comb in seen:
                        continue
                    queue.append(new_comb)
                    seen.add(new_comb)
            level += 1

        return -1
            
