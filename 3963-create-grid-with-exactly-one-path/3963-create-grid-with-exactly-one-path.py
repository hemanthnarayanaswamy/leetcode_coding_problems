class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res = []
        free = '.'
        block = '#'

        for i in range(m):
            if i:
                path = block * (n-1) + free
            else:
                path = free * n
            
            res.append(path)
        
        return res