class PrefixTree:

    def __init__(self):
        self.tree = {}
        self.ending = "#"

    def insert(self, word: str) -> None:
        sub_tree = self.tree
        for w in word:
            if w not in sub_tree:
                sub_tree[w] = {}
            sub_tree = sub_tree[w]
        sub_tree[self.ending] = {}

    def search(self, word: str) -> bool:
        sub_tree = self.tree
        for w in word:
            if w not in sub_tree:
                return False
            sub_tree = sub_tree[w]

        return self.ending in sub_tree

    def startsWith(self, prefix: str) -> bool:
        sub_tree = self.tree
        for w in prefix:
            if w not in sub_tree:
                return False
            sub_tree = sub_tree[w]

        return True
        