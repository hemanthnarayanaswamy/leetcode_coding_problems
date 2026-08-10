class Solution:
    def residuePrefixes(self, s: str) -> int:
        unique = set()
        res = 0

        for i in range(len(s)):
            c = s[i]
            unique.add(c)

            if len(unique) == (i+1) % 3:
                res += 1
        
        return res
