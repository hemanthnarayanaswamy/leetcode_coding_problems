class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()
        
        res = 0

        while grid[0]:
            tmp = []
            for row in grid:
                tmp.append(row.pop())
            res += max(tmp)
        
        return res