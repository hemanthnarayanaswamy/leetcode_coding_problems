class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        res = ''
        n = len(s)

        for i in range(n):
            encrypted = i+k

            while encrypted >= n:
                encrypted -= n

            res += s[encrypted]
        
        return res