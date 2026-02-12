class Solution:
    def isFascinating(self, n: int) -> bool:
        n2 = n * 2
        n3 = n * 3
        numsFreq = {}
    
        nums = (str(n) + str(n2) + str(n3))

        for num in nums:
            if num in numsFreq:
                return False
            elif num == '0':
                return False
            else:
                numsFreq[num] = 1
        
        return True
        
        
        