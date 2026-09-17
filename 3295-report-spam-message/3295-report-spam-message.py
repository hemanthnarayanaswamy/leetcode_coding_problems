class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        spamCount = 0
        freq = Counter(bannedWords)

        for word in message:
            if word in freq:
                spamCount += 1
        
        return spamCount >= 2