class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        profit_heap = []

        c_p = [(c, p) for p, c in zip(profits, capital)]
        c_p.sort()
        i = 0
        while k > 0:

            while i < len(c_p) and w >= c_p[i][0]:
                heapq.heappush(profit_heap, -c_p[i][1])
                i += 1
            if not profit_heap:
                break
            w += -heapq.heappop(profit_heap)
            k -= 1
        
        return w
