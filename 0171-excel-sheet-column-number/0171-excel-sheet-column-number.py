class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        temp = columnTitle[::-1]
        columnNum = 0

        for i in range(len(temp)):
            columnNum += (26 ** i)*(ord(temp[i])-64)
        
        return columnNum
