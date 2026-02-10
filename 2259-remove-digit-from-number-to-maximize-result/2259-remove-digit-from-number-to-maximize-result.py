class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        maxRes = '0'
        n = len(number)

        for i in range(len(number)):
            if number[i] == digit:
                tmp = number[0:i]+number[i+1:n]
                if tmp > maxRes:
                    maxRes = tmp
        
        return maxRes