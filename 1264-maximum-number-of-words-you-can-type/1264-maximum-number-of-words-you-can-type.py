class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        cannotType = 0

        for word in text:
            for char in brokenLetters:
                if char in word:
                    cannotType += 1
                    break
        
        return len(text) - cannotType
                