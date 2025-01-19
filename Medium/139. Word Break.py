class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        memo = {}

        def helper(sub_s):
            if sub_s in memo:
                return memo[sub_s]
            if not sub_s:
                return True

            for i in range(1, len(sub_s) + 1):
                if sub_s[:i] in word_set and helper(sub_s[i:]):
                    memo[sub_s] = True
                    return True

            memo[sub_s] = False
            return False

        return helper(s)
