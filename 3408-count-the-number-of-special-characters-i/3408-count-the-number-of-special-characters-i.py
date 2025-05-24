class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        result = 0

        for i in range(ord('a'), ord('z') + 1):
            x = chr(i)
            if x.lower() in word and x.upper() in word:
                result += 1
        
        return result
        
