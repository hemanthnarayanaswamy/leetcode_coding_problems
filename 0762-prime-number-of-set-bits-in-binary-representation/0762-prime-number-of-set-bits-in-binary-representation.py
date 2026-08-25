class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primeNums = {2, 3, 5, 7, 11, 13, 17, 19}
        res = 0

        for num in range(left, right+1):
            if bin(num).count('1') in primeNums:
                res += 1
        
        return res