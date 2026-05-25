class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l <= 1:
            return l

        result = 0
        seen = set()
        left = 0
        for right in range(l):
            if s[right] in seen:
                while s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                left += 1
            else:
                result = max(result, right - left + 1)
                seen.add(s[right])
        return result