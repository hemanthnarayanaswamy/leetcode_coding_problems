class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        s = 'abcdefghijklmnopqrstuvwxyz'
        res = ''
        i = len(s)-1

        for _ in range(n):
            while i + n > k:
                i -= 1
            res += s[i]
            k -= (i+1)
            n -= 1
        
        return res[::-1]
