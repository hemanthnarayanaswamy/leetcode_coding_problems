class Solution:
    def sumOfMultiples(self, n: int) -> int:
        result = 0
        
        for num in range(3, n+1):
            if num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
                result += num
        
        return result
