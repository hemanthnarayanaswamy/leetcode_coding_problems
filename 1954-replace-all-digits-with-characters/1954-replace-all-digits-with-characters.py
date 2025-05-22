class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)
        print(s)

        for i in range(1, len(s), 2):
            c, n = s[i-1], int(s[i])
            s[i] = chr(ord(c)+n)
        
        return "".join(s)
