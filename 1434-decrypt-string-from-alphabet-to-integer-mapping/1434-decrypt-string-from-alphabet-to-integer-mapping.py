class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s)-1
        result = []

        while i >= 0:
            if s[i] == '#':
                num = 96 + int(s[i-2:i])
                result.append(chr(num))
                i -= 3
            else:
                num = 96 + int(s[i])
                result.append(chr(num))
                i -= 1
        
        return ''.join(result[::-1])