class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s)< 3: return s

        a = s[0]
        b = s[1]
        res = [a, b]
        for c in s[2:]:
            if c == b == a:
                continue
            else:
                res.append(c)
            a, b = b, c
        return ''.join(res)