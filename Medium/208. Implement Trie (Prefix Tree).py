class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        prev = self.root

        for c in word:
            if c not in prev.children:
                prev.children[c] = TrieNode()
            prev = prev.children[c]
        prev.end = True

        return

    def search(self, word: str) -> bool:
        prev = self.root

        for c in word:
            if c not in prev.children:
                return False
            prev = prev.children[c]

        return True if prev.end == True else False

    def startsWith(self, prefix: str) -> bool:
        prev = self.root

        for c in prefix:
            if c not in prev.children:
                return False
            prev = prev.children[c]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
