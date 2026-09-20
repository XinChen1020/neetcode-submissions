class FreqStack:
    # list of stack
    # Imagine
    def __init__(self):
        self.stack_list = [deque()]
        self.counter = Counter()

    def push(self, val: int) -> None:
        self.counter[val] += 1

        if self.counter[val] > len(self.stack_list):
            self.stack_list.append(deque([val]))
        else:
            self.stack_list[self.counter[val] - 1].append(val)


    def pop(self) -> int:
        val = self.stack_list[-1].pop()
        self.counter[val] -= 1

        if not self.stack_list[-1]:
            self.stack_list.pop()
        
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()