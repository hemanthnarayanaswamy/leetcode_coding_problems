class Solution:
    def rotatedDigits(self, n: int) -> int:
        inValid = ('3', '4', '7')
        rotate = {'0': '0', '1': '1', '8': '8', '2': '5', '6': '9', '5': '2', '9': '6'}

        res = 0
        for i in range(1, n+1):
            s = str(i)

            if any(c in inValid for c in s):
                continue

            new = "".join(rotate[c] for c in s)

            if new != s:
                res += 1
            
        return res


