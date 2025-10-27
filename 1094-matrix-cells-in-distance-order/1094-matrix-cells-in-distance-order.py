class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        res = defaultdict(list)
        
        for i in range(rows):
            rdist = abs(rCenter - i)
            for j in range(cols):
                dist = rdist + abs(cCenter - j)
                res[dist].append([i, j])
        
        res = sorted(res.items())

        return [c for _,cor in res for c in cor]