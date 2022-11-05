# Trie was the right approach, but we need a method to remove word from the trie once it has been found
class Trie:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def add_word(self, w: str) -> None:
        cur = self
        for c in w:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.is_word = True
    
    def remove_word(self, w: str) -> None:
        cur = self
        parentNodechildKeyPairs = []
        for c in w:
            parentNodechildKeyPairs.append((cur, c))
            cur = cur.children[c]

        for parentNode, childKey in reversed(parentNodechildKeyPairs):
            targetNode = parentNode.children[childKey]
            if len(targetNode.children) == 0:
                del parentNode.children[childKey]
            else:
                return

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for w in words:
            trie.add_word(w)
        m, n = len(board), len(board[0])
        res = set()
        visited = set()
        
        def recSearch(i: int, j: int, t, word: str) -> None:
            if not((i >= 0) and (i < m) and (j >= 0) and (j < n) and (board[i][j] in t.children) and ((i, j) not in visited)):
                return
            visited.add((i, j))
            t = t.children[board[i][j]]
            word += board[i][j]
            if t.is_word:
                res.add(word)
                t.is_word = False
                trie.remove_word(word)
            recSearch(i - 1, j, t, word)
            recSearch(i + 1, j, t, word)
            recSearch(i, j - 1, t, word)
            recSearch(i, j + 1, t, word)
            visited.remove((i, j))
        for i in range(m):
            for j in range(n):
                recSearch(i, j, trie, "")
        return list(res)

    # TLE, even though everything is correct ... I had to write a different but apparently more optimized solution of the exact same code
    """
    def create_trie(self, words: List[str]) -> dict:
        trie = dict()
        for w in words:
            current_dict = trie
            for c in w:
                current_dict = current_dict.setdefault(c, {})
            current_dict["end"] = {}
        return trie

    def get_neighbors(self, i: int, j: int, m: int, n: int, path_taken: set) -> list:
        neighbors = []
        for k in (-1, 1):
            if ((i + k) >= 0) and ((i + k) < m) and ((i + k, j) not in path_taken):
                neighbors.append((i+k, j))
            if ((j + k) >= 0) and ((j + k) < n) and ((i, j + k) not in path_taken):
                neighbors.append((i, j+k))
        return neighbors

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = self.create_trie(words)
        res = set()
        m, n = len(board), len(board[0])
        def recSearch(i: int, j: int, trie: dict, current_word: str, path_taken: set) -> None:
            nonlocal res, board
            if board[i][j] not in trie:
                return
            if "end" in trie[board[i][j]]:
                res.add(current_word+board[i][j])
            for (k, l) in self.get_neighbors(i, j, m, n, path_taken):
                new_path = path_taken.copy()
                new_path.add((k, l))
                recSearch(k, l, trie[board[i][j]], current_word+board[i][j], new_path)

        for i in range(m):
            for j in range(n):
                path_taken = set([(i, j)])
                recSearch(i, j, trie, "", path_taken)
        return list(res)
    """
