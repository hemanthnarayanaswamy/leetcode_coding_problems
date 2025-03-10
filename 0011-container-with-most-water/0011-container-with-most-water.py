class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = []
        l, r = 0, len(heights)-1 
        while l < r:
            print(heights[l], heights[r],r,l, '------>', min(heights[l], heights[r])*(r-l))
            result.append(min(heights[l], heights[r])*abs(r-l))
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max(result)
        