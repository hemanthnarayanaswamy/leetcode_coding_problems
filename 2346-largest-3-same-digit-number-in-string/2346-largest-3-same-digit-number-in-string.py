class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i = 0
        maxNum = -1
        res = ''

        while i < len(num)-2:
            if num[i] == num[i + 1] == num[i + 2]:
                x = int(num[i])
                if x > maxNum:
                    maxNum = x
                    res = num[i:i+3]
                i += 3
            else:
                i += 1
                
        return res