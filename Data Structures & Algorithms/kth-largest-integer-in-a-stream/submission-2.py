class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        heapq.heapify(self.heap)
        self.k = k

        for item in nums:
            self.add(item)
    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
           heapq.heappop(self.heap) 
        return self.heap[0]
