class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s, p = 0, 1
        n = [int(num) for num in str(n)]
        
        for num in n:
            s += num
            p *= num
        
        return p - s