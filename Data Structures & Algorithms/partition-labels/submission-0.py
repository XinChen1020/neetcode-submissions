class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Start with the most common letter 
        remaining = Counter(s)

        # Letters that we have seen so far that still have remaining
        current = set()
        result = []
        l = -1
        # Keep going furthest until the count for all seen letter so far are 0
        for r in range(len(s)):
            
            current.add(s[r])
            remaining[s[r]] -= 1

            if remaining[s[r]] == 0:
                current.remove(s[r])

                if not current:
                    result.append(r - l)
                    l = r
        
        return result