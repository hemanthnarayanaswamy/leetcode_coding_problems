class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        symmetric = 0

        for x in range(low, high+1):
            num = [int(d) for d in str(x)]
            n = len(num)
            
            if n % 2:
                continue
            m = n // 2
           
            if sum(num[:m]) == sum(num[m:]):
                symmetric += 1
        
        return symmetric