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

            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]
                node.ref += 1

            node.end_of_word = True
            node.word = w

        return root

    def dfs(self, i, j, board, parent, path, results):
        ch = board[i][j]
        node = parent.children[ch]

        # path stores: parent, char_from_parent, current_node
        path.append((parent, ch, node))

        if node.end_of_word:
            results.append(node.word)

            node.end_of_word = False
            node.word = ""

            # This found word is no longer needed,
            # so decrement ref along the full prefix path.
            for _, _, path_node in path:
                path_node.ref -= 1

            # Delete the highest useless branch.
            for path_parent, path_ch, path_node in path:
                if path_node.ref == 0:
                    del path_parent.children[path_ch]
                    path.pop()
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
                self.dfs(ni, nj, board, node, path, results)

                # A deeper dfs may have deleted this whole branch.
                if node.ref == 0:
                    break

        board[i][j] = temp
        path.pop()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.build_trie(words)
        results = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                ch = board[i][j]

                if ch in root.children:
                    self.dfs(i, j, board, root, [], results)

        return results