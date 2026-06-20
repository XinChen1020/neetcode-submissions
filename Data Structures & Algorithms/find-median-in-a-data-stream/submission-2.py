class MedianFinder:

    def __init__(self):
        # max_heap -> lower half
        # min_heap -> higher half
        # Let top of max_heap to be the median when there's 
        # odd numbers and average of max_heap[0] and min_heap[0]
        # when there's even numbers
        self.max_heap = []
        self.min_heap = []

        # use for rebalance
        self.max_heap_size = 0
        self.min_heap_size = 0

    def addNum(self, num: int) -> None:
        # Fill in lower heap for initial element 
        if not self.min_heap:
            heapq.heappush(self.min_heap, num)
            self.min_heap_size += 1
            return
        
        if num > self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
            self.min_heap_size += 1
        else:
            heapq.heappush(self.max_heap, -num)
            self.max_heap_size += 1
        
        # rebalance
        if self.max_heap_size - self.min_heap_size > 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            self.max_heap_size -= 1
            self.min_heap_size += 1
        elif self.min_heap_size - self.max_heap_size >= 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
            self.min_heap_size -= 1
            self.max_heap_size += 1


    def findMedian(self) -> float:
        if self.max_heap_size == 0:
            return self.min_heap[0]

        return (-self.max_heap[0] + self.min_heap[0]) / 2 if self.max_heap_size == self.min_heap_size else -self.max_heap[0]
        
        