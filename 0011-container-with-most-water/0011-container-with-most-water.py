class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        water = 0

        while l < r:
            h = min(height[l], height[r])
            w = r - l
            water = max(water, h*w)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return water