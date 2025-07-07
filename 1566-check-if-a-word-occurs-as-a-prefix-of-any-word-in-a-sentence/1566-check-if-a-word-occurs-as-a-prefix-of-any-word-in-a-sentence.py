class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentenceLst = sentence.split()
        s = len(searchWord)

        res = -1

        for i, word in enumerate(sentenceLst):
            if searchWord == word[:s]:
                res = i + 1
                return res
        
        return res
