class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s)-1
        result = ''

        while i >= 0:
            if s[i] == '#':
                num = 96 + int(s[i-2:i])
                result += chr(num)
                print(s[i-2:i], result)
                i -= 3
            else:
                num = 96 + int(s[i])
                result += chr(num)
                print(s[i], result)
                i -= 1
        
        return result[::-1]