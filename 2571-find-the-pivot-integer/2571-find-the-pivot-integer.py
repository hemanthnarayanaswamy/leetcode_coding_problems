class Solution:
    def pivotInteger(self, n: int) -> int:
        leftSum = 0
        rightSum = 0

        totalSum = sum(range(1, n+1))

        for i in range(1, n+1):
            rightSum = totalSum - leftSum 
            leftSum += i

            if rightSum == leftSum:
                return i 
        
        return -1