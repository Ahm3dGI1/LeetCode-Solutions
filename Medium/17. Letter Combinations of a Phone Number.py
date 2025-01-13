class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        res = []

        def comb(curr, i):
            nonlocal res
            if i >= len(digits):
                if curr != "":
                    res.append(curr)
                return

            for c in m[digits[i]]:
                comb(curr + c, i+1)

        comb("", 0)

        return res
