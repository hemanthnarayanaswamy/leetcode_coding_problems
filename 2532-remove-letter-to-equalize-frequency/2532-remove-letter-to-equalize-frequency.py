class Solution:
    def equalFrequency(self, word: str) -> bool:
        if len(word) == len(set(word)):
            return True

        wordFreq = [val for val in Counter(word).values()]
        
        for i in range(len(wordFreq)):
            wordFreq[i] -= 1
            if len(set(wordFreq)) == 1:
                return True
            if wordFreq[i] == 0:
                if len(set(wordFreq)) == 2:
                    return True
            wordFreq[i] += 1
            
        return False
