class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += str(len(string)) + "#" + string
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i, j = 0, 0

        while i < len(s):
            # find the #
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]

            result.append(word)

            j += 1 + length
            i = j
        return result