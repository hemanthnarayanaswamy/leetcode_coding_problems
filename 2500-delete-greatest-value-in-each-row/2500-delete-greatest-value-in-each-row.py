class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()
        res = 0

        while grid[0]:
            maxNum = 0
            for row in grid:
                num = row.pop()
                if num > maxNum:
                    maxNum = num
            res += maxNum
        
        return res