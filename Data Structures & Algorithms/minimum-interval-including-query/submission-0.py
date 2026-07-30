class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # Build some sort of structure and then go through each query and get distance
        # Use min heap to keep track of minimal interval

        # Save queries location so we can map result back to the original order
        mapped_result = {}
        original_queries = queries.copy()
        
        intervals.sort()
        queries.sort()

        # Store (length, end of interval)
        # end of interval for tie breaker
        # since we want to popo
        min_heap = []
        i = 0

        for q in queries:

            # Push all valid intervals into the min heap
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(min_heap, \
                (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            # Before getting the answer, we also need to remove
            # invalid intervals
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            mapped_result[q] = min_heap[0][0] if min_heap else -1

        return [mapped_result[q] for q in original_queries]

