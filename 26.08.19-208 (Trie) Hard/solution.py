class Trie:
    def __init__(self):
        self.children = [[-1] * 26]
        self.is_end = [False]

    def insert(self, word: str) -> None:
        node = 0
        for w in word:
            idx = ord(w) - ord('a')

            if self.children[node][idx] == -1:
                self.children[node][idx] = len(self.children)
                self.children.append([-1] * 26)
                self.is_end.append(False)
            node = self.children[node][idx]
        self.is_end[node] = True

    def search(self, word: str) -> bool:
        node = 0
        for w in word:
            idx = ord(w) - ord('a')

            if self.children[node][idx] == -1:
                return False
            node = self.children[node][idx]
        return self.is_end[node]

    def startsWith(self, prefix: str) -> bool:
        node = 0
        for w in prefix:
            idx = ord(w) - ord('a')

            if self.children[node][idx] == -1:
                return False
            node = self.children[node][idx]
        return True