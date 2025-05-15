class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        startB = bin(start)[2:]
        goalB = bin(goal)[2:]
        flipCount = 0

        n = abs(len(startB) - len(goalB))

        if len(startB) > len(goalB):
            goalB = '0'*n+goalB
        else:
            startB = '0'*n+startB
        
        for i in range(len(goalB)):
            if goalB[i] != startB[i]:
                flipCount += 1
        
        return flipCount
