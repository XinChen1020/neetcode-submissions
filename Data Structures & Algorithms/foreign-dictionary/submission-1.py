class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Topological sort

        # Graph and degree calculation
        # u -> v if u < v
        # since we want from smallest to largest
        adj = {char: set() for word in words for char in word}
        in_degress = {char: 0 for word in words for char in word}

        for i in range(len(words)):
            for j in range(i, len(words)):

                if len(words[i]) > len(words[j]) and words[i].startswith(words[j]):
                    return ""

                for index, (char1, char2) in enumerate(zip(words[i], words[j])):
                    if char1 != char2:
                        if char2 not in adj[char1]:
                            adj[char1].add(char2)
                        
                            in_degress[char2] += 1
                        break

        queue = deque()
        for char, degree in in_degress.items():
            if degree == 0:
                queue.append(char)

        result = ""

        while queue:
            for _ in range(len(queue)):
                char = queue.popleft()
                result += char

                for nei in adj[char]:
                    in_degress[nei] -= 1
                    if in_degress[nei] == 0:
                        queue.append(nei)
        if len(result) != len(adj.keys()):
            return ""
        return result


