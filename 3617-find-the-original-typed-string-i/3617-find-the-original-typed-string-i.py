class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        answer = 1

        for i in range(1, n):
            if word[i-1] == word[i]:
                answer += 1
        
        return answer
        