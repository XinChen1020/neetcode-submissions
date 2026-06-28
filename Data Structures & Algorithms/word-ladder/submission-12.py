class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        def pattern(w):
            return [w[:i] + "*" + w[i + 1:] for i in range(len(w))]

        # Build wildcard pattern -> words
        adj = defaultdict(list)
        for w in wordList:
            for p in pattern(w):
                adj[p].append(w)

        # Need beginWord patterns too, since beginWord may not be in wordList
        for p in pattern(beginWord):
            adj[p].append(beginWord)

        # Bidirectional BFS
        begin_set = {beginWord}
        end_set = {endWord}

        visited_begin = {beginWord}
        visited_end = {endWord}

        count = 1

        while begin_set and end_set:
            # Always expand the smaller side
            if len(begin_set) > len(end_set):
                begin_set, end_set = end_set, begin_set
                visited_begin, visited_end = visited_end, visited_begin

            next_set = set()

            for word in begin_set:
                for p in pattern(word):
                    for nei in adj[p]:
                        if nei in visited_end:
                            return count + 1

                        if nei not in visited_begin:
                            visited_begin.add(nei)
                            next_set.add(nei)

            begin_set = next_set
            count += 1

        return 0