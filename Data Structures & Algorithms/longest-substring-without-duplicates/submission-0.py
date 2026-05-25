class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l <= 1:
            return l

        result = 0
        seen = set()
        right = 0
        for left in range(l):
            if s[left] in seen:
                while s[right] != s[left]:
                    seen.remove(s[right])
                    right += 1
                right += 1
            else:
                result = max(result, left - right + 1)
                seen.add(s[left])
        return result