class Solution:
    def possibleStringCount(self, word: str) -> int:
        total = 1
        consecutiveCount = 0
        previousChar = ''

        for i in range(len(word)):
            if word[i] != previousChar:
                total += consecutiveCount
                consecutiveCount = 0
                previousChar = word[i]
            else:
                consecutiveCount += 1
        
        if consecutiveCount:
            total += consecutiveCount
            
        return total