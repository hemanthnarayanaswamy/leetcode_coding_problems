class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        s = 'abcdefghijklmnopqrstuvwxyz'
        res = ''

        for _ in range(n):
            for i in range(len(s)-1, -1, -1):
                if i + n <= k:
                    res += s[i]
                    k -= (i+1)
                    n -= 1
                    break
        
        return res[::-1]
