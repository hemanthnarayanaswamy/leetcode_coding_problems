class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        for i, val in enumerate(nums):
            for j, val2 in enumerate(nums):
                if abs(val - val2) < valueDifference:
                    continue
                if abs(i -j) < indexDifference:
                    continue

                # if abs(val - val2) >= valueDifference and abs(i -j) >= indexDifference:
                return [i, j]
                
        return [-1, -1]