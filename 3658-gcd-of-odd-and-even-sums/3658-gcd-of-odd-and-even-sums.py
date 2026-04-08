class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumEven = n*(n+1)
        sumOdd = n**2

        return math.gcd(sumEven, sumOdd)