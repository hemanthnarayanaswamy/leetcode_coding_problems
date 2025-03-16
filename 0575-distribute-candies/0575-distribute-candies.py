class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType) 
        half = n // 2
        uniqueTypes = len(set(candyType))

        return half if half < uniqueTypes else uniqueTypes
        