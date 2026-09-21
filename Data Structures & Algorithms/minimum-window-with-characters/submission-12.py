class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needed = Counter(t)
        required = len(needed)

        current = {}
        having = 0

        min_length = float("inf")
        min_l = 0

        l = 0

        for r, char in enumerate(s):

            # Only track characters that matter
            if char in needed:
                current[char] = current.get(char, 0) + 1

                if current[char] == needed[char]:
                    having += 1

            while having == required:
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    min_l = l

                char_l = s[l]

                if char_l in needed:
                    current[char_l] -= 1

                    if current[char_l] < needed[char_l]:
                        having -= 1

                l += 1

        if min_length == float("inf"):
            return ""

        return s[min_l:min_l + min_length]