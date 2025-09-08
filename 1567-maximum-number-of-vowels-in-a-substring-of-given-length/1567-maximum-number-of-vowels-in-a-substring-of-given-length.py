class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        countVowel = maxVowels = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}

        for i in range(len(s)):
            if s[i] in vowels:
                countVowel += 1
            
            if i >= k:
                if s[i - k] in vowels:
                    countVowel -= 1
            
            maxVowels = max(countVowel, maxVowels)

        
        return maxVowels