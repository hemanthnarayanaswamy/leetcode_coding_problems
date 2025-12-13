class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = [tuple(grid[i]) for i in range(len(grid))]
        columns = list(zip(*grid))
        count = 0

        for col in columns:
            for row in rows:
                if col == row:
                    count += 1
        
        return count
