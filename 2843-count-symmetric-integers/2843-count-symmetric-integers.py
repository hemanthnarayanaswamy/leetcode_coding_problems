class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def numList(n):
            num = []
            l = 0
            while n:
                n, q = divmod(n, 10)
                num.append(q)
                l += 1
            return num, l

        symmetric = 0

        for x in range(low, high+1):
            num, n = numList(x)
            
            if n % 2:
                continue

            m = n // 2
           
            if sum(num[:m]) == sum(num[m:]):
                symmetric += 1
        
        return symmetric