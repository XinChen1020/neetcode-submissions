class WordDictionary:

    def __init__(self):
        self.trie: dict[str, dict] = {}
        self.ending = "#"
        self.wild = "."

    def addWord(self, word: str) -> None:
        sub_trie = self.trie

        for ch in word:
            if ch not in sub_trie:
                sub_trie[ch] = {}
            sub_trie = sub_trie[ch]

        sub_trie[self.ending] = {}

    def dfs(self, j, sub_trie, word) -> bool:
        cur = sub_trie

        for i in range(j, len(word)):
            ch = word[i]

            # Only do dfs when necessary
            # Otherwise, just loop through each letters for exact match
            if ch == self.wild:
                for key, child in cur.items():
                    if key != self.ending:
                        if self.dfs(i + 1, child, word):
                            return True
                return False

            else:
                if ch not in cur:
                    return False
                cur = cur[ch]

        return self.ending in cur

    def search(self, word: str) -> bool:
        return self.dfs(0, self.trie, word)