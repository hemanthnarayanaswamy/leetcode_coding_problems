class Solution:
    def maxFreqSum(self, s: str) -> int:
        maxV, maxC = 0, 0
        sFreq = Counter(s)
        vowels = 'aeiou'

        for char in s:
            if char in vowels:
                tempV =  sFreq[char]
                if tempV > maxV:
                    maxV = tempV
            else:
                tempC =  sFreq[char]
                if tempC > maxC:
                    maxC = tempC 
        
        return maxV + maxC
