from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # longest repeated substring with max of k replacement
        left = 0
        c = Counter()
        res = 0

        for right in range(len(s)):
            c[s[right]] += 1


            while (right - left + 1) - max(c.values()) > k:
                c[s[left]] -= 1

                left += 1


            res = max(res, right - left + 1)

        return res