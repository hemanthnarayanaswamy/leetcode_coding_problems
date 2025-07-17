class Solution:
    def stringHash(self, s: str, k: int) -> str:
        res = []
        lowerAscii = 97

        for i in range(0, len(s), k):
            tmp = 0
            for j in range(i, i+k):
                tmp += (ord(s[j]) - lowerAscii)
            
            tmp = (tmp % 26) + lowerAscii
            
            res.append(chr(tmp))
        
        return ''.join(res)
