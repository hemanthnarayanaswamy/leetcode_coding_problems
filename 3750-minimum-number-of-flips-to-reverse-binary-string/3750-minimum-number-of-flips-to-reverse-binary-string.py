class Solution:
    def minimumFlips(self, n: int) -> int:
        s=bin(n)[2:]
        rev=s[::-1]
        c=0
        for i in range(len(s)):
            if s[i]!=rev[i]:
                c+=1
        return c
            