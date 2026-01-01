class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        count = 0
        def negativeInx(arr):
            l, r = 0, n-1
            while l <= r:
                m = (l+r)//2
                if arr[m] >= 0:
                    l = m + 1
                else:
                    r = m - 1
            return l
        
        for arr in grid:
            count += (n - negativeInx(arr))
        
        return count
