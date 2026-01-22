class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        l, r = x, x + k - 1

        while l < r:
            grid[l][y:y+k], grid[r][y:y+k] = grid[r][y:y+k], grid[l][y:y+k]
            l += 1
            r -= 1
        
        return grid