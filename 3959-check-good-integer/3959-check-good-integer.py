class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        squareTotal = total = 0

        while n:
            n, m = divmod(n, 10)
            
            total += m
            squareTotal += m**2
        
        if squareTotal - total >= 50:
            return True
        else:
            return False