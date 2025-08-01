class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        res = [[1], [1, 1]]

        for _ in range(2, numRows):
            pre_row = [0] + res[-1] + [0]
            tmp = []

            for j in range(len(pre_row)-1):
                tmp.append(pre_row[j]+pre_row[j+1])
            
            res.append(tmp)

        return res
        