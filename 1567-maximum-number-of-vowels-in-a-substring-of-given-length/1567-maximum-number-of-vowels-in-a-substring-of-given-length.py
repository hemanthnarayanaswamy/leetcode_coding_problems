class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        countVowel = 0

        for c in s[:k]:
            if c in vowels:
                countVowel += 1
        
        maxVowels = countVowel

        for i in range(k, len(s)):
            if s[i] in vowels:
                countVowel += 1

            if s[i - k] in vowels:
                countVowel -= 1 
            
            if countVowel > maxVowels:
                    maxVowels = countVowel 

        return maxVowels