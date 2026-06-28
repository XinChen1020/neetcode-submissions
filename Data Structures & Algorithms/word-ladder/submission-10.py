class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # BFS but use wildcard patterns as key for adj list
        def pattern(w) -> List[str]:
            return [w[:i] + "*" + w[i + 1:] for i in range(len(w))]

        adj = defaultdict(list)
        for w in wordList:
            for p in pattern(w):
                adj[p].append(w)

        # Add beginWord to graph:
        for p in pattern(beginWord):
            adj[p].append(beginWord)
        
        # BFS
        # Since there might be cycles, we use visited 
        visited = set()
        queue = deque([beginWord])
        count = 0
        while queue:
            count += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                visited.add(node)

                if node == endWord:
                    return count

                for p in pattern(node):
                    for nei in adj[p]:
                        if nei == node or nei in visited:
                            continue
                        queue.append(nei)

        return 0
