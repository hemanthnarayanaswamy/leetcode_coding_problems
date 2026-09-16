class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        num = 1
        res = 1 

        for i in range(1, 8056):
            if num % k == 0:
                return res
            
            num = (num *10) + 1
            res += 1
        
        return -1