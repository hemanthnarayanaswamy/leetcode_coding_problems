class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        sfreq = Counter(secret)
        gfreq = Counter(guess)
        bulls = 0

        for s,g in zip(secret, guess):
            if s == g:
                bulls += 1
                sfreq[s] -= 1
                gfreq[g] -= 1
        
        cows = 0
        for c in sfreq:
            cows += min(sfreq[c], gfreq[c])
        
        return str(bulls)+'A'+str(cows)+'B'
        

