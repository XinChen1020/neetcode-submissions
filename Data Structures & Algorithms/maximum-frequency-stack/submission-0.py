from collections import Counter
class FreqStack:
    # heap + idx
    # Heap to keep track of most frequent element
    # Use idx (order added into the stack) to break the even when frequence is equal
    def __init__(self):

        self.heap = []
        self.counter = Counter()
        self.idx = 0
        

    def push(self, val: int) -> None:
        self.counter[val] += 1

        heapq.heappush(self.heap, [-self.counter[val], -self.idx, val])

        self.idx += 1

    def pop(self) -> int:
        
        _, _, val = heapq.heappop(self.heap)
        self.counter[val] -= 1

        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()