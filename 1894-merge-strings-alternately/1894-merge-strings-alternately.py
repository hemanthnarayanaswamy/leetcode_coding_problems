class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        i, j = 0, 0
        len_word1 = len(word1)
        len_word2 = len(word2)

        while len(result) != len_word1 + len_word2:
            if i < len_word1:
                result += word1[i]
                i += 1
            if j < len_word2:
                result += word2[j]
                j += 1 
        return result
            