class Solution:
    def fib(self, n: int) -> int:
        def fib(n):
            if n in d:
                return d[n]
            else:
                return fib(n-1) + fib(n-2)
        d={}
        d[0]=0
        d[1]=1

        return fib(n)
