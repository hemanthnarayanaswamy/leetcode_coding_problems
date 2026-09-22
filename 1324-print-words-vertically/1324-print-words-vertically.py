class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(len(word) for word in words)
        res = []

        for i in range(max_len):
            newWord = ''
            for word in words:
                if i < len(word):
                    newWord += word[i]
                else:
                    newWord += " "
            res.append(newWord.rstrip())
        
        return res
            