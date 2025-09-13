class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        maxWins = 0
        idx = -1

        for i in range(n):
            wins = 0
            for j in range(n):
                if i != j and grid[i][j] == 1:
                    wins += 1
            if wins > maxWins:
                maxWins = wins
                idx = i
        
        return idx