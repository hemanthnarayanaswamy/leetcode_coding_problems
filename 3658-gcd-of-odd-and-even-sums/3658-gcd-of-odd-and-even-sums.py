class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        a = n*(n+1)
        b = n**2

        while b:
            a, b = b, a%b
        
        return a