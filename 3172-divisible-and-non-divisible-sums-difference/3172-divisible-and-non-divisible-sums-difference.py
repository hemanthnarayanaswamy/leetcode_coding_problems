class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1, num2 = 0, 0

        i = 1

        while i < n+1:
            if i % m == 0:
                num2 += i
            else:
                num1 += i
            i += 1
        
        return num1 - num2
            