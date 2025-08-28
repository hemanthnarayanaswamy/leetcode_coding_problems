class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        gridMap = defaultdict(list)
        n = len(grid)

        for i in range(n):
            for j in range(n):
                gridMap[i-j].append(grid[i][j])
        
        for k in gridMap:
            if k < 0: 
                gridMap[k].sort(reverse=True)
            else:
                gridMap[k].sort()

        for i in range(n):
            for j in range(n):
                grid[i][j] = gridMap[i-j].pop()
                
        return grid