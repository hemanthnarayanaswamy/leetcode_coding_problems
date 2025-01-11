class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1],]

        for row in range(numRows-1): ## because we have already filled one row 
            temp = [0] + result[-1] + [0]
            row = []
            for i in range(len(result[-1]) + 1):
                row.append(temp[i]+ temp[i+1])
            result.append(row)
        return result
        