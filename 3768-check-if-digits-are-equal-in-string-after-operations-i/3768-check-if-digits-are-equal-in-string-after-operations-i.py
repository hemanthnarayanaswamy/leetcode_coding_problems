class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = [int(x) for x in s]
        while len(s) > 2:
            newS = []
            for i in range(len(s)-1):
                tmp = (s[i] + s[i+1]) % 10
                newS.append(tmp)
            s = newS
        
        return s[0] == s[1]


           
        