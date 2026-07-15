class Solution:
    def fib(self, n: int) -> int:
        def fib(n):
            if n in d:
                return d[n]
            d[n] = fib(n-1) + fib(n-2)
            return d[n]
            
        d={}
        d[0]=0
        d[1]=1

        return fib(n)
