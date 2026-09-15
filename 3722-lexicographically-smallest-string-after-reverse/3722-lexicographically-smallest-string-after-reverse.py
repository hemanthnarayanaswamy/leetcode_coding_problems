class Solution:
    def lexSmallest(self, s: str) -> str:
        n = len(s)
        res = s

        for i in range(n):
            tmp1 = s[:i][::-1] + s[i:]
            tmp2 = s[:i]+ s[i:][::-1] 
            
            if tmp1 > tmp2:
                tmp1 = tmp2
            
            if res > tmp1:
                res = tmp1

        return res
