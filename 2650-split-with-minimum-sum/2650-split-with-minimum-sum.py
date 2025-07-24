class Solution:
    def splitNum(self, num: int) -> int:
        num1 = []
        num2 = []

        num = sorted(str(num))

        for i in range(len(num)):
            if i % 2:
                num2.append(num[i])
            else:
                num1.append(num[i])
        
        num1 = int(''.join(num1))
        num2 = int(''.join(num2))

        return num1 + num2