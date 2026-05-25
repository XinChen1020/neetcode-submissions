from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # longest repeated substring with max of k replacement
        left = 0
        c = Counter()
        res = 0

        for right in range(len(s)):
            c[s[right]] += 1

            maxFreq = max(c.values())

            while (right - left + 1) - maxFreq > k:
                c[s[left]] -= 1

                if c[s[left]] == 0:
                    del c[s[left]]

                left += 1

                # Recompute after shrinking, because maxFreq may have changed
                maxFreq = max(c.values()) if c else 0

            res = max(res, right - left + 1)

        return res