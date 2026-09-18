class Solution:
    def numTimesAllBlue(self, flips: list[int]) -> int:
        n = len(flips)
        maxSeen = -1
        res = 0

        for i in range(n):
            f = flips[i]
            
            if f > maxSeen:
                maxSeen = f
            
            if maxSeen == i+1:
                res += 1
        
        return res
            
            