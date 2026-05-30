class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        op = {'+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: int(x / y)}
        
        for t in tokens:
            if t in op:
                n_1, n_2 = stack.pop(), stack.pop()

                stack.append(op[t](n_2, n_1))
            else:
                stack.append(int(t))
        return stack[0]