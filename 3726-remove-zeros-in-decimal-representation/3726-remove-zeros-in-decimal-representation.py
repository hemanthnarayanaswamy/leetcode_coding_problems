class Solution:
    def removeZeros(self, n: int) -> int:
        res = 0

        for i in str(n):
            if i != '0':
                res = res * 10 + int(i)
        
        return res
