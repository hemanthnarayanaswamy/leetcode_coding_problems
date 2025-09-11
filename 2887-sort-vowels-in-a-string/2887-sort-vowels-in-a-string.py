class Solution:
    def sortVowels(self, s: str) -> str:
        s_vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        s = list(s)
        temp = []
        for i in range(len(s)):
            if s[i] in s_vowel:
                temp.append(s[i])
                s[i] = '_'
        temp.sort(reverse=True)

        for i in range(len(s)):
            if s[i] == '_':
                s[i] = temp.pop()
        
        return ''.join(s)