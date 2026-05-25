class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(s)) + "#" + s for s in strs])

    def decode(self, s: str) -> List[str]:
        result = []
        c = 0
        s_len = len(s)

        while c < s_len:
            
            # Reading length
            if s[c].isdigit():
                total_l = ""
                while s[c].isdigit():
                    total_l += s[c]
                    c += 1
                total_l = int(total_l)
            # skip "#"
            c += 1

            # Reading words
            curr_w = ""
            while total_l > 0:
                curr_w += s[c]
                total_l -= 1
                c += 1
            result.append(curr_w)
        return result