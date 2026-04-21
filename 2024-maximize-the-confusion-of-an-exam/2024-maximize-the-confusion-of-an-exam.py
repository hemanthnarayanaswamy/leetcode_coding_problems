class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def countConsecutives(key):
            left = 0
            maxLen = count = 0


            for right in range(len(answerKey)):
                if answerKey[right] == key:
                    count += 1

                while count > k:
                    if answerKey[left] == key:
                        count -= 1
                    left += 1
                
                maxLen = max(maxLen, right - left + 1)
            
            return maxLen
        
        return max(countConsecutives('T'), countConsecutives('F'))
