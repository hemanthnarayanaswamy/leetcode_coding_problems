class Solution:
    def checkDivisibility(self, n: int) -> bool:
        num = n
        arr = []

        while num:
            q, r = divmod(num, 10)
            arr.append(r)
            num = q
        
        s = sum(arr)
        p = 1
        for i in arr:
            p *= i
        
        return n % (s+p) == 0

