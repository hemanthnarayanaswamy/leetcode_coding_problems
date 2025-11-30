class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        minVal = float('inf')

        for i, num in enumerate(nums):
            if num == target:
                tmpVal = abs(i - start)
                if tmpVal < minVal:
                    minVal = tmpVal
        
        return minVal