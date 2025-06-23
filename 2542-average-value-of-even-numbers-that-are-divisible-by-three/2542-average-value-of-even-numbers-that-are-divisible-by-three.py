class Solution:
    def averageValue(self, nums: List[int]) -> int:
        avgsum  = []

        for num in nums:
            if num % 2: 
                continue 
            
            if num % 3:
                continue 

            avgsum.append(num)
        
        return sum(avgsum) // len(avgsum) if avgsum else 0

