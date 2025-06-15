class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        combinedWords = s1.split() + s2.split()
        wordCounts = Counter(combinedWords)

        result = [word for word, freq in wordCounts.items() if freq == 1]
        return result