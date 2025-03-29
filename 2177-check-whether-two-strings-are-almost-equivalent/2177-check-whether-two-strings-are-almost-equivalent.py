from collections import Counter 

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        word1_freq = Counter(word1)
        word2_freq = Counter(word2)

        for letter in set(word1+word2):
            if abs(word1_freq.get(letter, 0) - word2_freq.get(letter, 0)) > 3:
                return False
        return True
        