class Solution:
    def sortVowels(self, s: str) -> str:
        s_vowel = {'a', 'e', 'i', 'o', 'u'}
        s = list(s)
        temp = []
        for i in range(len(s)):
            if s[i].lower() in s_vowel:
                temp.append(s[i])
                s[i] = '*'
        temp.sort(reverse=True)

        for i in range(len(s)):
            if s[i] == '*':
                s[i] = temp.pop()
        
        return ''.join(s)
        