class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right = 0, 0
        c_required = Counter(t)
        c_current = Counter()
        filled = 0
        min_length = len(s) + 1
        result = ""
        s_len = len(s)
        while right < s_len:
            if s[right] in c_required:
                c_current[s[right]] += 1

                if c_current[s[right]] == c_required[s[right]]:
                    filled += 1
                if filled == len(c_required.keys()):
                     
                    while True:
                        if s[left] in c_required:
                            if c_required[s[left]] == c_current[s[left]]:
                                break
                            c_current[s[left]] -= 1
                        left += 1

                    if right - left + 1 < min_length:
                        min_length = right - left + 1
                        result = s[left:right + 1]
                    filled -= 1
                    c_current[s[left]] -= 1
                    left += 1
            
            right += 1
        
        return result
            