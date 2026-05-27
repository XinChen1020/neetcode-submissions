from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = Counter(t)
        window = Counter()

        have = 0
        need = len(required)

        best_len = float("inf")
        best_l = 0

        left = 0

        for right, ch in enumerate(s):
            window[ch] += 1

            if ch in required and window[ch] == required[ch]:
                have += 1

            while have == need:
                # current window is valid
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_l = left

                # shrink from the left
                left_ch = s[left]
                window[left_ch] -= 1
                if left_ch in required and window[left_ch] < required[left_ch]:
                    have -= 1

                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_l: best_l + best_len]