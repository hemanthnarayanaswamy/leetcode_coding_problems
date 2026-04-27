class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        symmetric = 0

        for x in range(low, high+1):
            x = str(x)
            n = len(x)
            if n % 2:
                continue

            num = [int(d) for d in x]
            m = n // 2
           
            if sum(num[:m]) == sum(num[m:]):
                symmetric += 1
        
        return symmetric