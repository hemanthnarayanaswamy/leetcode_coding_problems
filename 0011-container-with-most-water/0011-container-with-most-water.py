class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        water = 0

        while l < r:
            h = height[l] if height[l] < height[r] else height[r]
            w = r - l

            volume = h * w
            if volume > water:
                water = volume
        
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return water