class Solution:
    def decodeString(self, s: str) -> str:
        number_stack = deque()
        letter_stack = deque()
        k = 0
        cur = ""

        for l in s:
            if l.isdigit():
                k = k * 10 + int(l)
            
            # Stact new recording
            elif l == "[":
                letter_stack.append(cur)
                number_stack.append(k)
                k = 0
                cur = ""
            
            # resolve
            elif l == "]":
                letter = letter_stack.pop()
                number = number_stack.pop()
                
                cur = letter + cur * number
            else:
                cur += l

        return cur