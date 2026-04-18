class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
            
        nonZero = []
        dig = ''

        while n:
            d, m = divmod(n, 10)
            n = d
            if m != 0:
                nonZero.append(m)
                dig += str(m)
        
        total = sum(nonZero)
        dig = int(dig[::-1])

        return dig*total
            