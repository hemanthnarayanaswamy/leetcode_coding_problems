class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        spamCount = 0
        banned = set(bannedWords)

        for word in message:
            if word in banned:
                spamCount += 1
        
        return spamCount >= 2