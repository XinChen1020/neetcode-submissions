class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Sliding window, Required

        needed = Counter(t)
        required = len(needed.keys())

        current = Counter()
        having = 0

        min_length = float("inf")
        result = ""
        l = 0

        for r in range(len(s)):
            current[s[r]] += 1
            if current[s[r]] == needed[s[r]]:
                having += 1
            
            while having == required:
                if r - l + 1 < min_length:
                    result = s[l:r + 1]
                    min_length = r - l + 1

                current[s[l]] -= 1

                if current[s[l]] < needed[s[l]]:
                    having -= 1

                l += 1
        
        return result

            