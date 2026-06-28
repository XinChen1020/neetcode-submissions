class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def patterns(w):
            return [w[:i] + "*" + w[i + 1:] for i in range(len(w))]

        adj = defaultdict(list)
        for w in wordList:
            for p in patterns(w):
                adj[p].append(w)

        # beginWord may not be in wordList
        for p in patterns(beginWord):
            adj[p].append(beginWord)

        q1 = deque([beginWord])
        q2 = deque([endWord])

        visited1 = {beginWord}
        visited2 = {endWord}

        count = 1

        while q1 and q2:
            # expand smaller side
            if len(q1) > len(q2):
                q1, q2 = q2, q1
                visited1, visited2 = visited2, visited1

            # expand ONE level
            for _ in range(len(q1)):
                word = q1.popleft()

                for p in patterns(word):
                    for nei in adj[p]:
                        if nei in visited2:
                            return count + 1

                        if nei not in visited1:
                            visited1.add(nei)
                            q1.append(nei)

            count += 1

        return 0