class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        z = [0] * n 

        for i in range(1, n):
            p = 0 

            while p + i < n and s[p] == s[i+p]:
                p += 1
            
            if i + p == n and n % i == 0:
                return True
        
        return False
