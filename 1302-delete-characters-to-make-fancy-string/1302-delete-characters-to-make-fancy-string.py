class Solution:
    def makeFancyString(self, s: str) -> str:
        fancyStr = [s[0]]

        for i in range(1, len(s)):
            if i + 1 == len(s):
                fancyStr.append(s[i])
                continue 

            if s[i] == s[i-1] == s[i+1]:
                continue 
            fancyStr.append(s[i])
        
        return ''.join(fancyStr)
