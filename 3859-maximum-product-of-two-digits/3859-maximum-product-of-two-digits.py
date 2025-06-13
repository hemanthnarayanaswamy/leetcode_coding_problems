class Solution:
    def maxProduct(self, n: int) -> int:
        arr = sorted([int(i) for i in str(n)])
        
        return arr[-1]*arr[-2]
