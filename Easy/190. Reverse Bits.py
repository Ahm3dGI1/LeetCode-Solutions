class Solution:
    def reverseBits(self, n: int) -> int:
        inp = f'{n:032b}'

        res = 0

        for i in range(len(inp)):
            if inp[i] == "1":
                res += 2**i

        return res
