class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        total = 0

        for x in range(max(n-k ,0) , n+k+1):
            if (n & x) == 0:
                total += x
        
        return total