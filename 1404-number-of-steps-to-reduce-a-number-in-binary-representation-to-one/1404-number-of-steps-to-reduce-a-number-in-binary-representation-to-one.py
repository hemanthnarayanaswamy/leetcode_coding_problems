class Solution:
    def numSteps(self, s: str) -> int:
        sInt = int(s, 2)
        count = 0

        while sInt != 1:
            if sInt % 2:
                sInt += 1
            else:
                sInt //= 2
            count += 1
        
        return count
        