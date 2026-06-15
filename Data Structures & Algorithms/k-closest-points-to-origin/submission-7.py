class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # min heap
        heap =[]
        heapq.heapify(heap)
        current_len = 0
        for i in range(len(points)):
            x, y = points[i]
            distance = x ** 2 + y **2
            heapq.heappush(heap, (-distance, points[i]))
            current_len += 1
            if current_len > k:
                heapq.heappop(heap)
                current_len -= 1
        
        return [t[1] for t in heap]