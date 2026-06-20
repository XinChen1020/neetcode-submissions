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
        if not self.max_heap:
            heapq.heappush(self.max_heap, -num)
            self.max_heap_size += 1
            return

        # Doesn't matter which one to compare to 
        # as long as rebalanced afterward.
        if num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
            self.max_heap_size += 1
        else:
            heapq.heappush(self.min_heap, num)
            self.min_heap_size += 1
        
        # rebalance
        if self.max_heap_size - self.min_heap_size > 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            self.max_heap_size -= 1
            self.min_heap_size += 1
        # Assume max_heap[0] includes median in odd case, then
        # max_heap should always have >= 1 element than min_heap
        elif self.min_heap_size - self.max_heap_size >= 1:
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
            self.min_heap_size -= 1
            self.max_heap_size += 1


    def findMedian(self) -> float:

        return (-self.max_heap[0] + self.min_heap[0]) / 2 if self.max_heap_size == self.min_heap_size else -self.max_heap[0]
        
        