class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []

        for p in arr:
            distance = abs(p - x)

            # Root = furthest point
            # Tie: larger point is worse
            heapq.heappush(heap, (-distance, -p, p))

            if len(heap) > k:
                heapq.heappop(heap)

        result = [p for _, _, p in heap]
        result.sort()
        return result