class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(s)) + "#" + s for s in strs])

    def decode(self, s: str) -> List[str]:
        result = []
        c = 0
        s_len = len(s)

        while c < s_len:
            index = s.find("#", c)
            total_l = int(s[c:index])

            result.append(s[index + 1: index + 1 + total_l])
            c = index + 1 + total_l
        return result