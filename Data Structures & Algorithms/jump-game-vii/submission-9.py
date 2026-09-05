class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        queue = deque([0])

        farthest = 0

        while queue:
            idx = queue.popleft()

            start = max(idx + minJump, farthest + 1)
            end = min(idx + maxJump, n - 1)

            for nxt in range(start, end + 1):
                if s[nxt] == "0":
                    if nxt == n - 1:
                        return True
                    queue.append(nxt)

            farthest = max(farthest, end)

        return False