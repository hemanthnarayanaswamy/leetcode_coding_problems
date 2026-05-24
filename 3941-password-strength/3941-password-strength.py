class Solution:
    def passwordStrength(self, password: str) -> int:
        uniq = set(password)
        score = 0
        
        for c in uniq:
            if c.islower():
                score += 1
            elif c.isupper():
                score += 2
            elif c.isdigit():
                score += 3
            else:
                score += 5
        
        return score