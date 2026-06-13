class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        # (# of "(" need to user, # of ")" need to use, current result)
        stack = deque([[n, n, ""]])

        while stack:
            left_available, right_available, path = stack.pop()

            if left_available == 0 and right_available == 0:
                result.append(path)
                continue
            
            # Left parenthesis
            if left_available > 0:
                stack.append([left_available - 1, right_available, path + "("])

            # Right parenthesis
            # Must have "(" in front in order to consider put in ")"
            if right_available > 0 and left_available < right_available:
                stack.append([left_available, right_available - 1, path + ")"])
            
        return result