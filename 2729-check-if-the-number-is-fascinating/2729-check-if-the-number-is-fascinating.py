class Solution:
    def isFascinating(self, n: int) -> bool:
        n2 = n * 2
        n3 = n * 3
        numsFreq = set()
    
        nums = (str(n) + str(n2) + str(n3))

        for num in nums:
            if num in numsFreq or num == '0':
                return False
            else:
                numsFreq.add(num)
        
        return True
        
        
        