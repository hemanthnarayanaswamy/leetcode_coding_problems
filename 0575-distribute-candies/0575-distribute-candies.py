class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType) 
        uniqueTypes = len(set(candyType))

        return n//2 if n//2 < uniqueTypes else uniqueTypes
        