class Solution:
    def decodeString(self, s: str) -> str:
        sn = []
        ss = []
        currN = ""
        res = ""

        for c in s:
            if c in "1234567890":
                currN += c
            elif c == "[":
                sn.append(currN)
                currN = ""
                ss.append("")
            elif c == "]":
                psn = sn.pop()
                pss = ss.pop()
                if len(ss) == 0:
                    res += int(psn) * pss
                else:
                    ss[-1] += int(psn) * pss
            else:
                if not ss:
                    ss.append("")
                ss[-1] += c

        if ss:
            res += ss[-1]

        return res
