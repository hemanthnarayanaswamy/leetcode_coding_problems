class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        s = 'abcdefghijklmnopqrstuvwxyz'
        res = ['a'] * n
        p = 25

        for i in range(len(res)):
            while p + n > k:
                p -= 1
            res[i] = s[p]
            k -= (p+1)
            n -= 1
        
        return ''.join(res[::-1])
