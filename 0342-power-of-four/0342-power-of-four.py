class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        elif n > 1:
            while n > 1:
                if n % 4 != 0:
                    return False
                n //= 4
        else:
            return False
        
        return True