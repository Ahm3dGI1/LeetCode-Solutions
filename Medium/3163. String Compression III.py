class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        count = 0
        curr = word[0]
        for i in range(len(word)):
            if curr == word[i] and count < 9:
                count += 1
            else:
                comp += str(count) + curr
                count = 1
                curr = word[i]

        comp += str(count) + curr
        count = 1
        curr = word[i]

        return comp
