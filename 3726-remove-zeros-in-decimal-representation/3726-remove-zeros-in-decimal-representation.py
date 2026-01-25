class Solution:
    def removeZeros(self, n: int) -> int:
        res = []

        for i in str(n):
            if i != '0':
                res.append(i)
        
        return int(''.join(res))
