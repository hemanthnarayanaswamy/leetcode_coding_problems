class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)

        i = 0

        while i < 2:
            if s1[i] != s2[i]:
                s1[i], s1[i+2] = s1[i+2], s1[i]
            i += 1
        
        return s1 == s2