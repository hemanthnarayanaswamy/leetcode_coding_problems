class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = []
        l, r = 0, len(heights)-1 
        while l < r:
            result.append(min(heights[l], heights[r])*abs(r-l))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max(result)
        