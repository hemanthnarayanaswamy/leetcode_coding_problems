class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digitProduct(num):
            arr = []

            while num:
                num, m = divmod(num, 10) 
                arr.append(m)
            
            ans = 1
            for a in arr:
                ans *= a
            
            return ans
        
        for num in range(n, n+11):
            prod = digitProduct(num)

            if prod % t == 0:
                return num
                