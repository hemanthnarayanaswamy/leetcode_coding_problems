class Solution:
    def getSmallestString(self, s: str) -> str:
        res = s
        n = len(s)

        for i in range(n-1):
            a, b = s[i], s[i+1]

            if int(a) % 2 == int(b) % 2 and b < a:
                num = s[:i]+b+a+s[i+2:] 
                if num < res:
                    res = num

        return res
