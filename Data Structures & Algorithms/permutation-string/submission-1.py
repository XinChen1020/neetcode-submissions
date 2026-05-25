from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        c_s1 = Counter(s1)
        s1_len = len(s1)
        current = Counter(s2[:s1_len])

        for right in range(s1_len , len(s2)):
            if c_s1 == current:
                return True
            
            current[s2[right]] += 1
            current[s2[right - s1_len]] -= 1
        
        return False if c_s1 != current else True
