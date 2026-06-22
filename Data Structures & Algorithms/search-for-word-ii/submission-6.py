class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_word = False
        self.word = ""
        self.ref = 0


class Solution:
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def build_trie(self, words):
        root = TrieNode()

        for w in words:
            node = root
            node.ref += 1

            for c in w:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
                node.ref += 1

            node.end_of_word = True
            node.word = w

        return root

    def dfs(self, i, j, board, parent, ch, results):
        node = parent.children[ch]

        if node.ref == 0:
            return

        if node.end_of_word:
            results.append(node.word)
            node.end_of_word = False

            # Found this word, so this exact node has one fewer remaining word.
            node.ref -= 1

            # If no remaining word uses this node/subtree, remove it.
            if node.ref == 0:
                del parent.children[ch]
                return

        temp = board[i][j]
        board[i][j] = "#"

        for di, dj in self.directions:
            ni = i + di
            nj = j + dj

            if (
                0 <= ni < len(board)
                and 0 <= nj < len(board[0])
                and board[ni][nj] in node.children
            ):
                self.dfs(ni, nj, board, node, board[ni][nj], results)

        board[i][j] = temp

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.build_trie(words)
        results = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                ch = board[i][j]
                if ch in root.children:
                    self.dfs(i, j, board, root, ch, results)

        return results