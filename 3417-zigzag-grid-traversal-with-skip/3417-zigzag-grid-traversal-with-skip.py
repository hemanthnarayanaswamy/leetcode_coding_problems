class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res = []
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            if i % 2:
                start, end, step = n-1, -1, -1
            else:
                start, end, step = 0, n, 1
            for j in range(start, end, step):
                if i % 2 == j % 2:
                        res.append(grid[i][j])
        
        return res