class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        z = [0] * n 
        l = r = 0

        for i in range(1, n):
            if i <= r:
                mirror = i - l
                z[i] = min(z[mirror], r - i + 1)
            
            while z[i] + i < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            
            if i + z[i] - 1 > r:
                l = i
                r = i + z[i] - 1
            
            if i + z[i] == n and n % i == 0:
                return True 
        
        return False