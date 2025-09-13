class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        winsCount = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and grid[i][j] == 1:
                    winsCount[i] += 1
        maxWins = 0
        idx = -1

        for i, w in enumerate(winsCount):
            if w > maxWins:
                idx = i
                maxWins = w
        
        return idx