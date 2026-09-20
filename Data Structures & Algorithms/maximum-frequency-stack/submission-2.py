class FreqStack:
    def __init__(self):
        self.stack_list = []
        self.counter = Counter()

    def push(self, val: int) -> None:
        self.counter[val] += 1
        freq = self.counter[val]

        if freq > len(self.stack_list):
            self.stack_list.append(deque())

        self.stack_list[freq - 1].append(val)

    def pop(self) -> int:
        val = self.stack_list[-1].pop()
        self.counter[val] -= 1

        if not self.stack_list[-1]:
            self.stack_list.pop()

        return val