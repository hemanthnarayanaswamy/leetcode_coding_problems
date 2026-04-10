class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        prime = [2, 3, 5, 7, 13, 17, 19, 31]

        for i in prime:
            n = 2**(i-1) * (2**i - 1)

            if n == num:
                return True
            elif n > num:
                return False
        
        return False