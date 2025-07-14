class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        numsFreq = {}
        n = len(grid)
        total = n * n

        for nums in grid:
            for num in nums:
                numsFreq[num] = numsFreq.get(num, 0) + 1
        
        for num, fq in numsFreq.items():
            if fq == 2:
                repeated_num = num 
        
        for num in range(1, total+1):
            if num not in numsFreq:
                missing_num = num 
        
        return [repeated_num, missing_num]
                
        
        
        
