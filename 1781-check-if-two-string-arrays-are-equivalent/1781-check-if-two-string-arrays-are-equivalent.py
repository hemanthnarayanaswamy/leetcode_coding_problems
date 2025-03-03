class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1 = "".join(word1)
        word2 = "".join(word2)

        if len(word1) != len(word2):
            return False 
        
        
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                return False
          
        return True
        