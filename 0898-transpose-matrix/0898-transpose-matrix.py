class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [] 

        for j in range(len(matrix[0])):
            tmp = []
            for i in range(len(matrix)):
                tmp.append(matrix[i][j])
            res.append(tmp)
        
        return res