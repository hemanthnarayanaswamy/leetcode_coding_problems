class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            newS = ''
            for i in range(len(s)-1):
                tmp = (int(s[i]) + int(s[i+1])) % 10
                newS += str(tmp)
            s = newS
        
       
        return s[0] == s[1]


           
        