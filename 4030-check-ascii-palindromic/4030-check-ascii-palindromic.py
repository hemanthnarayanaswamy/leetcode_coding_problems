class Solution:
    def isPalindromic(self, s: str) -> bool:
        binaryStr = ''

        for c in s:
            key = ord(c)
            b = bin(key)
            binaryStr += ('0'+b[2:]) # to make it 8 bit representation
        
        return binaryStr == binaryStr[::-1]