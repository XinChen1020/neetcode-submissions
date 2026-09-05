class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        if s[-1] == "1":
            return False
        
        # idx
        # Keep track of valid idx to scan for next level
        queue = deque([0])
        seen = set()
        while queue:

            for _ in range(len(queue)):
                idx = queue.popleft()

                if idx == len(s) - 1:
                    return True
                
                
                for jump in range(minJump, maxJump + 1):

                    if idx + jump >= len(s) or \
                    s[idx + jump] == "1" or \
                    idx + jump in seen:
                        continue
                    seen.add(idx + jump)
                    queue.append(idx + jump)

        return False