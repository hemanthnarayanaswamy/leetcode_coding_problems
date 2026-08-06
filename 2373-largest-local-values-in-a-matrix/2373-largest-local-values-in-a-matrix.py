class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0 for _ in range(n-2)] for _ in range(n-2)]

        for i in range(n-2):
            for j in range(n-2):
                largest = 0

                for r in range(0, 3):
                    for c in range(0, 3):
                        largest = max(largest, grid[i+r][j+c])
                
                ans[i][j] = largest
        
        return ans