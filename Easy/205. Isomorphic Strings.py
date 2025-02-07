class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ms = {}
        mt = {}
        for i in range(len(s)):
            if s[i] not in ms:
                ms[s[i]] = t[i]
            else:
                if ms[s[i]] != t[i]:
                    return False
            if t[i] not in mt:
                mt[t[i]] = s[i]
            else:
                if mt[t[i]] != s[i]:
                    return False

        return True
