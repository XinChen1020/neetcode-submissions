class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        record = {')': '(', '}': '{', ']': '['}

        for i in s:
            if i in record:
                if stack and stack[-1] == record[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        
        return False if stack else True