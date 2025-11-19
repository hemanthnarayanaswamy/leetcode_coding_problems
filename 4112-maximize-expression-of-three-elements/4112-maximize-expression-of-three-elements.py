class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        mx1 = mx2 = -inf
        mn = inf 

        for x in nums:
            if x > mx1:
                mx2 = mx1
                mx1 = x
            elif x > mx2:
                mx2 = x
            
            if x < mn:
                mn = x
        
        return mx1 + mx2 - mn
        