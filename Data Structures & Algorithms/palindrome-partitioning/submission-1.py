class Solution:
    def is_palindrome(self, s, l, r) -> bool:
        return s[l:r] == s[l:r][::-1]

    def partition(self, s: str) -> List[List[str]]:

        result = []
        stack = deque([[0, []]])

        while stack:
            # l = start of the next partition
            l, partitions = stack.pop()

            
            if l >= len(s):
                result.append(partitions)

            # Find the next potential partitions and add
            # to the list
            # r = end of the next partition/substring
            for r in range(l + 1, len(s) + 1):
                # Prune out partition if it's not forming a pailndrome
                if self.is_palindrome(s, l, r):
                    next_partitions = partitions.copy()
                    next_partitions.append(s[l:r])
                    stack.append([r, next_partitions])

        return result
    