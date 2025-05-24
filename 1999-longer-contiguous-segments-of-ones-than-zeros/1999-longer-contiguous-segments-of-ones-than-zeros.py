class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        countOne, countZero = 0, 0
        tempOne, tempZero = 0, 0

        for char in s:
            if char == '1':
                if tempOne == 0:
                    countZero = max(countZero, tempZero)
                    tempZero = 0
                tempOne += 1
            else:
                if tempZero == 0:
                    countOne = max(countOne, tempOne)
                    tempOne = 0
                tempZero += 1

        countOne = max(countOne, tempOne)
        countZero = max(countZero, tempZero)
        print(countOne, countZero)
        
        return countOne > countZero


