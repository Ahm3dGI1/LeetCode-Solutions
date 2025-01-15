class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        m = {}

        res = 0

        for i in range(len(words)):
            inv = words[i][1] + words[i][0]

            if inv in m and m[inv] > 0:
                res += 4
                m[inv] -= 1
            else:
                m[words[i]] = m.get(words[i], 0) + 1

        for item in m:
            if item[0] == item[1] and m[item] % 2 == 1:
                res += 2
                break

        return res
