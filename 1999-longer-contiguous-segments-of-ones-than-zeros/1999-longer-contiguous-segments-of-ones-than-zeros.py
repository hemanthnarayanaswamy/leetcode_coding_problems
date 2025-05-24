class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        countOne, countZero = 0, 0
        tempOne, tempZero = 0, 0

        for char in s:
            if char == '1':
                tempOne += 1
                tempZero = 0
            else:
                tempZero += 1
                tempOne = 0

            countOne = max(countOne, tempOne)
            countZero = max(countZero, tempZero)

        return countOne > countZero


