class Solution:
    def maxOperations(self, s: str) -> int:
        n, total, ones, i = len(s), 0, 0, 0
        while(i < n):
            if(s[i] == '0'):
                total += ones
                while(i < n and s[i] != '1'):
                    i += 1
            ones += 1
            i += 1
        return total
        