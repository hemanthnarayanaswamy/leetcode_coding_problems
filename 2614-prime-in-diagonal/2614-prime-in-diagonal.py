class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def isPrime(num):
            if num<= 1:
                return False
            for i in range(2, int(num**0.5)+1): # for i in range(2, int(math.sqrt(num))+1):
                if num % i == 0:
                    return 0
            return num
        
        res = 0
        n = len(nums)

        for i in range(n):
            num1 = nums[i][i]
            num2 = nums[i][n - i - 1]
            res = max(res, isPrime(num1), isPrime(num2))
        
        return res
