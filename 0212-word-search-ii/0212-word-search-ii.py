class TrieNode:
    def __init__(self):
        self.children = {}
        self.ends = False

class Solution:

    def __init__(self):
        self.root = TrieNode()

    def insert_into_trie(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.ends = True

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.insert_into_trie(word)

        root = self.root
        ROWS, COLS = len(board), len(board[0])
        ans = set()
        visit = set()

        def dfs(r, c, node, word):
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visit or
                board[r][c] not in node.children
            ):
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.ends:
                ans.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c - 1, node, word)

            visit.remove((r, c))
        
        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, root, "")

        return list(ans)


        