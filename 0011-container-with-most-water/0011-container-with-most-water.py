class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        l, r = 0, len(heights)-1 
        while l < r:
            max_area = min(heights[l], heights[r])*abs(r-l)
            if result < max_area:
                result = max_area
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return result
        