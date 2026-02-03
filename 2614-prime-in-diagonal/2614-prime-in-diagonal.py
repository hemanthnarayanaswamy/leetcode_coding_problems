class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def isPrime(num):
            if num<= 1:
                return False
            for i in range(2, int(num**0.5)+1): # for i in range(2, int(math.sqrt(num))+1):
                if num % i == 0:
                    return False
            return True
        
        res = 0
        n = len(nums[0])
        m = len(nums)

        for i in range(m):
            for j in range(n):
                if i == j or i + j == n - 1:
                    num = nums[i][j]
                    if num > res and isPrime(num):
                        res = num
        
        return res
