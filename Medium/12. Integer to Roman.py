class Solution:
    def intToRoman(self, num: int) -> str:
        m = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I",
        }

        res = ""

        for key in m:
            if num == 0:
                break
            count = num // key
            res += m[key] * count
            num -= key * count

        return res
