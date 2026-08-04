class Solution:
    def reverseWords(self, s: str) -> str:
        vowels = 'aeiouAEIOU'

        def countVowels(word):
            count = 0
            for c in word:
                if c in vowels:
                    count += 1
            
            return count
        
        s = s.split()
        refCount = countVowels(s[0])

        for i in range(1, len(s)):
            if countVowels(s[i]) == refCount:
                s[i] = s[i][::-1]
        
        return ' '.join(s)



            