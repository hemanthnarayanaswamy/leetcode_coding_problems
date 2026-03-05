class Solution:
    def minOperations(self, s: str) -> int:
        res = 0
        n = len(s)


        for i in range(n):
           if s[i] != ('1' if i % 2 else '0'):
                res += 1
        
        return min(res, n-res)