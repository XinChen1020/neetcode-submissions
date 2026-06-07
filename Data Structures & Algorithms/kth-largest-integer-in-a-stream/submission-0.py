class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        heapq.heapify(self.heap)
        self.k = k

        for item in nums:
            self.add(item)
    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        else:
            heapq.heappushpop(self.heap, val) 
        return self.heap[0]
