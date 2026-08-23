class Solution:
    def isPalindromic(self, s: str) -> bool:
        binaryStr = ''

        for c in s:
            key = ord(c)
            b = bin(key)
            print(b)
            binaryStr += ('0'+b[2:])
        
        return binaryStr == binaryStr[::-1]