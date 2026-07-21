class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        vowels = 'aeiou'
        vowelSum = 0
        
        for i in range(n):
            if word[i] in vowels:
                pre = i
                post = n - i - 1
                combined = pre * post

                vowelSum += pre + post + combined + 1
        
        return vowelSum



            
