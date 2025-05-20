class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x *= -1
        
       
        x = int(str(x)[::-1])

        if x > 2**31:
            return 0

        return (x*-1) if negative else x