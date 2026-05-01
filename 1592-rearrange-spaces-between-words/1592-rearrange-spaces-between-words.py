class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaceCount = text.count(" ")

        if spaceCount == 0:
            return text

        words = text.split()
        n = len(words)
        if n - 1 <= 0:
            words.extend([" "]*spaceCount)
            return "".join(words)

        d, m = divmod(spaceCount, n-1)

        res = []
        for i in range(n):
            res.append(words[i])
            if i != n - 1:
                res.extend([" "]*d)
        
        if m:
            res.extend([" "]*m)
        
        return "".join(res)