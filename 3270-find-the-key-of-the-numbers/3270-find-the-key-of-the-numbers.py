class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        def appendMissing(num):
            s = str(num)
            n = len(s)
            s = '0'*(4-n) + s
            return s
        
        num1 = appendMissing(num1)
        num2 = appendMissing(num2)
        num3 = appendMissing(num3)

        res = []

        for a,b,c in zip(num1, num2, num3):
            res.append(min(a,b,c))
        
        return int(''.join(res))