class Solution:
    def isBalanced(self, num: str) -> bool:
        oddSum = evenSum =  0

        for i in range(len(num)):
            if i % 2:
                oddSum += int(num[i])
            else:
                evenSum += int(num[i])
        
        return oddSum == evenSum