class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        n = len(grid)
        maxWins = 0
        idx = -1

        for i in range(n):
            wins = grid[i].count(1)

            if wins > maxWins:
                maxWins = wins
                idx = i
        
        return idx