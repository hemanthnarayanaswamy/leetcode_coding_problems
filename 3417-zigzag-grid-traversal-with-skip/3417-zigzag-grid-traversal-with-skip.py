class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        res = []
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            tmp = []
            for j in range(n):
                if i % 2 == 0:
                    if j % 2 == 0:
                        tmp.append(grid[i][j])
                else:
                    if j % 2:
                        tmp.append(grid[i][j])
            
            if i % 2:
                tmp = tmp[::-1]
            res.extend(tmp)
        
        return res