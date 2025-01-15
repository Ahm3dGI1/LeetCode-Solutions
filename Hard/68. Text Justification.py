class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line, length = [], 0
        i = 0

        while i < len(words):
            if length + len(line) + len(words[i]) > maxWidth:
                spaces = (maxWidth - length) // max(1, len(line) - 1)
                extraSpaces = (maxWidth - length) % max(1, len(line) - 1)

                finalLine = ""
                for j in range(len(line)):
                    finalLine += (line[j])
                    if j != len(line)-1 or len(line) == 1:
                        finalLine += " " * spaces
                        if extraSpaces:
                            finalLine += " "
                            extraSpaces -= 1

                res.append(finalLine)
                length = 0
                line = []

            line.append(words[i])
            length += len(words[i])
            i += 1

        finalLine = " ".join(line)
        space = maxWidth - length - (len(line)-1)
        finalLine += " "*space

        res.append(finalLine)

        return res
