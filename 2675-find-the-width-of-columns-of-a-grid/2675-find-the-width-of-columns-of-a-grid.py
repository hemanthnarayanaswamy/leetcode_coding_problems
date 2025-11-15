class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        ans = []
        n = len(grid[0])
        m = len(grid)

        for j in range(n):
            longest = 0
            for i in range(m):
                x = len(str(grid[i][j]))
                if x > longest:
                    longest = x
            ans.append(longest)
        
        return ans
