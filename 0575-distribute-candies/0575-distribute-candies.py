class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType) 
        unique_candies = set(candyType)

        return min(n//2, len(unique_candies))
        