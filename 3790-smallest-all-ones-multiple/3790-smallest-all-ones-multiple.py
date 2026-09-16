class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if k % 2 == 0: # even k can't divide 11...
            return -1

        seen = {1}
        num = 1
        count = 1

        while num % k != 0:
            num = ((num * 10)+1) % k 
            if num in seen:
                return -1
                
            seen.add(num)
            count += 1
        
        return count
        

