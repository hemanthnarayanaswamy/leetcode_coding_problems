class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        uniqSecret = set()
        bulls = cows = 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            uniqSecret.add(secret[i])
        
        
        for c in uniqSecret:
            cows += min(secret.count(c), guess.count(c))
        
        return str(bulls)+'A'+str(cows-bulls)+'B'
        

