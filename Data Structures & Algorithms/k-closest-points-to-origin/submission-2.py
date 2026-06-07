class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # min heap
        heap =[]
        heapq.heapify(heap)

        for i in range(len(points)):
            x, y = points[i]
            distance = math.sqrt(x ** 2 + y **2)
            heapq.heappush(heap, (-distance, points[i]))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [t[1] for t in heap]