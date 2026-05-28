class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        record = {')': '(', '}': '{', ']': '['}

        for i in s:
            if i in record:
                if not stack or stack[-1] != record[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        
        return True if not stack else False