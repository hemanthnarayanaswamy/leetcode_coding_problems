class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split()
        n = len(sentence)

        if n == 1:
            return sentence[0][0] == sentence[0][-1]
        
        for i in range(n-1):
                if sentence[i][-1] != sentence[i+1][0]:
                    return False
        
        return sentence[n-1][-1] == sentence[0][0]

