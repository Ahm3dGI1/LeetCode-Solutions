class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        m = defaultdict(int)
        word_len = len(words[0])
        substr_len = len(words) * word_len

        if substr_len > len(s):
            return []

        for i in range(len(words)):
            m[words[i]] += 1

        for i in range(len(s) - substr_len + 1):
            curr_m = defaultdict(int)
            for j in range(i, substr_len+i, word_len):
                curr_word = s[j:j+word_len]
                if curr_word in m:
                    curr_m[curr_word] += 1

                    if curr_m[curr_word] > m[curr_word]:
                        break
                else:
                    break
            else:
                res.append(i)

        return res
