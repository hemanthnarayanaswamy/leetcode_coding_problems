class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        nums = []

        for i in range(m):
            for j in range(n):
                nums.append(grid[i][j])

        res = [1]*(n*m)

        prefix = 1
        for i in range(n*m):
            res[i] = prefix
            prefix = (prefix * nums[i]) % 12345
        
        postfix = 1
        for i in range((n*m)-1, -1, -1):
            res[i] = (res[i] * postfix) % 12345
            postfix = (postfix * nums[i]) % 12345
        
        i = 0
        prodMat = []
        for _ in range(m):
            tmp = []
            for _ in range(n):
                tmp.append(res[i])
                i += 1
            prodMat.append(tmp)

        return prodMat
