class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        upperWord = word.upper()
        lowerWord = word.lower()
        captialWord = word.capitalize()

        if word == upperWord:
            return True
        elif word == lowerWord:
            return True 
        elif word == captialWord:
            return True 
        else:
            return False