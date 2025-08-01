class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1],]

        for i in range(2, numRows+1):
            ref = [0] + res[-1] + [0]
            tmp = []

            for j in range(len(ref)-1):
                tmp.append(ref[j]+ref[j+1])
            
            res.append(tmp)

        return res
        