class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False 
        
        vowel, cons = False, False
        
        for c in word:
            if c.isalnum():
                if not c.isnumeric():
                    if c in "AEIOUaeiou":
                        vowel = True
                    else:
                        cons = True
            else:
                return False
        
        return vowel and cons
                
                
