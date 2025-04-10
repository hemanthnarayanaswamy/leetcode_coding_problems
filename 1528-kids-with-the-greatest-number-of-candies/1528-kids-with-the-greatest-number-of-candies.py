class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        result = [False] * n
        present_greater = max(candies)

        for i in range(n):
            if candies[i] + extraCandies >= present_greater:
                result[i] = True
        
        return result
