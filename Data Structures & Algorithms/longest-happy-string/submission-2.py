class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = ""

        # (frequency, letter)
        heap = [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heap = [(i, j) for i, j in heap if i != 0]
        heapq.heapify(heap)
        print(heap)

        
        while heap:
            frequency, letter = heapq.heappop(heap)

            if len(result) >= 2 and result[-1] == letter and result[-2] == letter:
                if not heap:
                    return result
                temp = (frequency, letter)
                frequency, letter = heapq.heappop(heap)
                heapq.heappush(heap, temp)

            result += letter
            frequency += 1
            
            if frequency < 0:
                heapq.heappush(heap, (frequency, letter))
            
        return result