class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {}
        for i in range(len(s)):
            last_index[s[i]] = i

        result = []
        size = 0
        end = 0

        for i , c in enumerate(s):
            size += 1
            end = max(end, last_index[c])

            # Went through all letters in the curent greedy range
            # when it reach the end, every letter appeared in the 
            # greedy range should be included in the current partition 
            # so we add to the result
            if i == end:
                result.append(size)
                size = 0
        return result