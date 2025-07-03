class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []

        for c in s:
            if len(res) >= 2 and res[-2] == res[-1] == c:
                continue
            res.append(c)
        
        return ''.join(res)
