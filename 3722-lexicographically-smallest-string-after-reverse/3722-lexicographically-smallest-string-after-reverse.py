class Solution:
    def lexSmallest(self, s: str) -> str:
        n = len(s)
        res = s

        for i in range(n):
            tmp1 = s[:i][::-1] + s[i:]
            tmp2 = s[:i]+ s[i:][::-1] 
            res = min(tmp1, tmp2, res)

        return res
