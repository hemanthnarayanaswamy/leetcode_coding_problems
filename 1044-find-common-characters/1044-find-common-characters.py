class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        commonCharacters = Counter(words[0])
        n = len(words)

        for i in range(1, n):
            currentCharacters = Counter(words[i])

            for ch in commonCharacters:
                commonCharacters[ch] = min(currentCharacters[ch], commonCharacters[ch])
        
        for k, v in commonCharacters.items():
            while v:
                res.append(k)
                v -= 1
        
        return res
        
        