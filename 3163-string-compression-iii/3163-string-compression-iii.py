class Solution:
    def compressedString(self, word: str) -> str:
        if not word: 
            return ""

        res = []
        prev_c = word[0]
        count = 0

        for c in word:
            if prev_c == c and count < 9:
                count += 1
            else:
                res.append(str(count))
                res.append(prev_c)
                prev_c = c
                count = 1

        res.append(str(count))
        res.append(prev_c)

        return "".join(res)