class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s)< 3: return s

        res = [s[0], s[1]]

        for i in range(2, len(s)):
            if res[-2] == res[-1] == s[i]:
                continue
            res.append(s[i])
        
        return ''.join(res)