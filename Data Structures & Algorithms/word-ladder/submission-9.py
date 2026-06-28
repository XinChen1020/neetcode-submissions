class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Create a grph such that two word connected when
        # only one position diff
        # minimum path -> BFS


        # Construct undirected graph
        def diff_by_one(u, v) -> bool:
            mismatch = 0
            for i , j in zip(u, v):
                if i != j:
                    mismatch += 1
                    if mismatch > 1:
                        return False
            return True

        adj = defaultdict(list)
        for i in range(len(wordList)):
            # Avoid duplicate edges
            for j in range(i + 1, len(wordList)):
                if diff_by_one(wordList[i], wordList[j]):
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])


        # Add beginWord to graph:
        for w in wordList:
            if diff_by_one(beginWord, w):
                adj[w].append(beginWord)
                adj[beginWord].append(w)
        
        if beginWord not in adj or endWord not in adj:
            return 0
        
        # BFS
        # Since there might be cycles, we use visited 
        visited = set()
        queue = deque([beginWord])
        result = 0
        while queue:
            result += 1
            for _ in range(len(queue)):
                node  = queue.popleft()
                visited.add(node)

                if node == endWord:
                    return result
                for nei in adj[node]:
                    if nei in visited:
                        continue
                    queue.append(nei)

        return 0

            


