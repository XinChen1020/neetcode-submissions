from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        
        # Most frequent letter first
        # Use heap to keep track of most frequent letter
        counter = Counter(s)
        heap = []
        result = ""

        for letter, freq in counter.items():
            heapq.heappush(heap, (-freq, letter))
        
        while heap:
            neg_freq, letter = heapq.heappop(heap)

            if result and letter == result[-1]:
                if not heap:
                    return ""

                temp = (neg_freq, letter)
                neg_freq, letter = heapq.heappop(heap)
                heapq.heappush(heap, temp)

            neg_freq += 1
            result += letter
            if neg_freq < 0:
                heapq.heappush(heap, (neg_freq, letter))
        return result

