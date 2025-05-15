class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        wordsFreq = Counter(words)
        prefixCount = 0
        i = 0
        while i < len(s):
            pre = s[:i+1]
            if pre in wordsFreq:
                prefixCount += wordsFreq[pre]
            i += 1
        
        return prefixCount

        