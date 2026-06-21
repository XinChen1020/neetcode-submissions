class WordDictionary:

    def __init__(self):
        self.trie: dict[str,dict] = {}
        self.ending = "#"
        self.wild = "."
    def addWord(self, word: str) -> None:
        sub_trie = self.trie

        for w in word:
            if w not in sub_trie:
                sub_trie[w] = {}
            sub_trie = sub_trie[w]
        sub_trie[self.ending] = {}
        
    def dfs(self, word, sub_trie) -> bool:

        if not word:
            return self.ending in sub_trie
        if word[0] == self.wild:
            for k, v in sub_trie.items():
                if k != self.ending:
                    if self.dfs(word[1:], v):
                        return True
        else:
            if word[0] not in sub_trie:
                return False

            return self.dfs(word[1:], sub_trie[word[0]])
        
        return False

    def search(self, word: str) -> bool:
        return self.dfs(word, self.trie)

