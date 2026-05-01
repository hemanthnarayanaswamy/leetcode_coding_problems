class Solution:
    def reorderSpaces(self, text: str) -> str:
        spaceCount = text.count(" ")

        if spaceCount == 0:
            return text

        words = text.split()
        n = len(words)
        if n == 1:
            return words[0] + " " * spaceCount
        
        d, m = divmod(spaceCount, n-1)

        res = (" "*d).join(words)
        if m:
            res += " "*m
            
        return res