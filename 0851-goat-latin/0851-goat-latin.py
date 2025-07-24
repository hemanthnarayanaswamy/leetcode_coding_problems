class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        if not sentence:
            return ""
        
        res = []
        
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        
        for i, word in enumerate(sentence.split()):
            if word[0] in vowels:
                res.append(word + 'ma' + (i+1) * 'a')
            else:
                res.append(word[1::] + word[0] + 'ma' + (i+1) * 'a')
        
        return " ".join(res)


