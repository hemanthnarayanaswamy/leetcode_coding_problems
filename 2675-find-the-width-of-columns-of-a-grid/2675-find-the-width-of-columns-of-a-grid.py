class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        ans = []
        n = len(grid[0])
        m = len(grid)

        for j in range(n):
            tmp = 0
            for i in range(m):
                tmp = max(tmp, len(str(grid[i][j])))
            ans.append(tmp)
        
        return ans

