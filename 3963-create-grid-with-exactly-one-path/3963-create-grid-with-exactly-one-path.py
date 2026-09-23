class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res = []

        for i in range(m):
            if i == 0:
                res.append('.'*n)
            else:
                res.append('#'*(n-1)+'.')
        
        return res