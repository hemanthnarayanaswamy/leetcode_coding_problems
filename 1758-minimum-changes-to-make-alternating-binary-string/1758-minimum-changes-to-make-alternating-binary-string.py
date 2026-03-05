class Solution:
    def minOperations(self, s: str) -> int:
        res1 = 0

        for i in range(len(s)):
           if s[i] != ('1' if i % 2 else '0'):
                res1 += 1
        
        return min(res1, len(s)-res1)