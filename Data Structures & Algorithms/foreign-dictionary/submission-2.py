class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Topological sort

        adj = {char: set() for word in words for char in word}
        in_degrees = {char: 0 for word in words for char in word}

        # Compare adjacent words only
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            # Invalid prefix case
            if len(word1) > len(word2) and word1.startswith(word2):
                return ""

            # Find FIRST different character
            for char1, char2 in zip(word1, word2):
                if char1 != char2:
                    if char2 not in adj[char1]:
                        adj[char1].add(char2)
                        in_degrees[char2] += 1

                    # Ordering is decided now
                    break

        queue = deque()

        for char, degree in in_degrees.items():
            if degree == 0:
                queue.append(char)

        result = ""

        while queue:
            char = queue.popleft()
            result += char

            for nei in adj[char]:
                in_degrees[nei] -= 1

                if in_degrees[nei] == 0:
                    queue.append(nei)

        # Cycle
        if len(result) != len(adj):
            return ""

        return result