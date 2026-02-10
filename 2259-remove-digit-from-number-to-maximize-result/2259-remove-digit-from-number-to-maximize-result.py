class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        maxRes = set()
        n = len(number)

        for i in range(len(number)):
            if number[i] == digit:
                maxRes.add(number[0:i]+number[i+1:n])
        
        return max(maxRes)