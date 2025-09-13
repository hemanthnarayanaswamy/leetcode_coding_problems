class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        maxWins = idx = 0

        for i in range(len(grid)):
            wins = grid[i].count(1)

            if wins > maxWins:
                maxWins = wins
                idx = i
        
        return idx