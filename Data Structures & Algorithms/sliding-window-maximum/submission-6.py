class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Heap plus sliding window
        if len(nums) <= k:
            return [max(nums)]

        result = []

        # -number, idx
        heap = []
        l = 0
        for r in range(len(nums)):
            heapq.heappush(heap, [-nums[r], r])

            if r - l + 1 < k:
                continue
            
            # collect result
            while heap[0][1] < l:
                heapq.heappop(heap)
            
            result.append(-heap[0][0])
            l += 1
        
        return result
            

