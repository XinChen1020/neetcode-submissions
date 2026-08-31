class StockSpanner:
    
    def __init__(self):
        # monotonic decreasing stack -> previous greater
        self.stack = deque()
        self.curr_idx = 0
        

    def next(self, price: int) -> int:
        self.curr_idx += 1

        if not self.stack:
            self.stack.append((self.curr_idx, price))
            return 1
        
        while self.stack and price >= self.stack[-1][1]:
            self.stack.pop()
        
        result = self.curr_idx
        if self.stack:
            result -= self.stack[-1][0]

        self.stack.append((self.curr_idx, price))
        return result
        





# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)