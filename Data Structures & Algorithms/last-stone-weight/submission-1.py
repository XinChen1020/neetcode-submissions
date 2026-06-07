class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            remain_stone = (-heapq.heappop(stones)) - (-heapq.heappop(stones))
            heapq.heappush(stones, -remain_stone)
            
        
        return -stones[0]