class Solution:
    def getRow(self, index: int) -> List[int]:
        result = [[1],]
        for row in range(index):
            temp = [0] + result[-1] + [0]
            currentRow = []
            for j in range(len(result[-1])+1):
                currentRow.append(temp[j] + temp[j+1])
            result.append(currentRow)
        return result[index]