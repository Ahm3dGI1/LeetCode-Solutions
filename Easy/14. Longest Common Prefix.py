class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]

        for s in strs:
            if len(res) > len(s):
                res = res[:len(s)]
            for i in range(len(s)):
                if i >= len(res):
                    break
                if s[i] != res[i]:
                    res = res[:i]
                    break
            if res == "":
                break

        return res
