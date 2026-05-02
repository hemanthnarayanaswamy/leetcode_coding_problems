class Solution:
    def rotatedDigits(self, n: int) -> int:
        inValid = ('3', '4', '7')
        rotate = {'0': '0', '1': '1', '8': '8', '2': '5', '6': '9', '5': '2', '9': '6'}

        res = 0
        for i in range(1, n+1):
            s = str(i)
            new = ''
            if '3' in s or '4' in s or '7' in s:
                continue
            for c in s:
                new += rotate[c]
            
            if new and new != s:
                res += 1
        
        return res


