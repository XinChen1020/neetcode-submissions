class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Heap sort 

        heap = []
        result = []

        for n in nums:
            heapq.heappush(heap, n)
        
        while heap:
            result.append(heapq.heappop(heap))
        
        return result
