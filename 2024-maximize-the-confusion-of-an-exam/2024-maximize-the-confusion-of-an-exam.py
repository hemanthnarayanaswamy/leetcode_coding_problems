class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        left = 0
        countT = countF = 0
        maxLen = 0

        for right in range(n):
            if answerKey[right] == 'T':
                countT += 1
            else:
                countF += 1
            
            while min(countT, countF) > k:
                if answerKey[left] == 'T':
                    countT -= 1
                else:
                    countF -= 1
                left += 1
            
            maxLen = max(maxLen, right-left+1)
        
        return maxLen