class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_len = len(s1)
        need = [0] * 26
        window = [0] * 26

        for ch in s1:
            need[ord(ch) - ord('a')] += 1

        for ch in s2[:s1_len]:
            window[ord(ch) - ord('a')] += 1

        if need == window:
            return True

        for right in range(s1_len, len(s2)):
            window[ord(s2[right]) - ord('a')] += 1
            window[ord(s2[right - s1_len]) - ord('a')] -= 1

            if need == window:
                return True

        return False