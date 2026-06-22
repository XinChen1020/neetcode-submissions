class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_word = False

        # Used for the word collected so it's easier to return
        self.word = ""


class Solution:
    search_direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def build_trie(self, words) -> TrieNode:
        root = TrieNode()

        for w in words:
            sub_trie = root
            for c in w:
                if c not in sub_trie.children:
                    sub_trie.children[c] = TrieNode()
                sub_trie = sub_trie.children[c]

            sub_trie.end_of_word = True
            sub_trie.word = w


        return root
    
    def dfs(self, i, j, board, sub_trie) -> list[str]:
        results = []

        if sub_trie.end_of_word:
            results.append(sub_trie.word)

        # no end of word mark and no children to keep exploring, 
        # abondon current branch
        if not sub_trie.children:
            return results

        for d in self.search_direction:
            new_i = i + d[0]
            new_j = j + d[1]

            if 0 <= new_i < len(board) and \
            0 <= new_j < len(board[0]) and \
            board[new_i][new_j] in sub_trie.children:
                # Mark to it wouldn't look back
                temp = board[i][j]
                board[i][j] = "#"

                results += self.dfs(new_i, new_j, board, sub_trie.children[board[new_i][new_j]])
                
                # Restore
                board[i][j] = temp
        return results


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Use Trie tree for search word O(N)
        # Use dfs for searching

        results = set()
        # Build the trie
        root = self.build_trie(words)

        # Do the dfs
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.children:
                    results.update(self.dfs(i, j, board, root.children[board[i][j]]))
        return list(results)
