class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        columns = list(zip(*grid))
        count = 0

        for row in grid:
            for col in columns:
                if row == list(col):
                    count += 1
        
        return count
