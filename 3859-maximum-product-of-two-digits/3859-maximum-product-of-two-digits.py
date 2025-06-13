class Solution:
    def maxProduct(self, n: int) -> int:
        firstMax, secondMax = 0, 0
        
        arr = [int(i) for i in str(n)]

        for num in arr:
            if num > firstMax:
                secondMax = firstMax
                firstMax = num
            elif num > secondMax:
                secondMax = num 
        
        return firstMax * secondMax