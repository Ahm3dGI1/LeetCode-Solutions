from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        q = deque([(beginWord, 1)])
        done = set([beginWord])

        while q:
            curr, currRes = q.popleft()

            if curr == endWord:
                return currRes

            for i in range(len(curr)):
                original_char = curr[i]
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == original_char:
                        continue
                    newWord = curr[:i] + c + curr[i+1:]
                    if newWord in wordSet and newWord not in done:
                        q.append((newWord, currRes + 1))
                        done.add(newWord)

        return 0
