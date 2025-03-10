class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        l, r = 0, len(heights)-1 
        while l < r:
            if heights[l] < heights[r]:
                max_area = heights[l]*(r-l)
                l += 1
            else:
                max_area = heights[r]*(r-l)
                r -= 1
            if result < max_area:
                result = max_area
        
        return result
        