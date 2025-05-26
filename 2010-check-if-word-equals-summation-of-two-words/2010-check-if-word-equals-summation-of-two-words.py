class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        alphabet = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}
        x, y, z = '', '', ''

        for w in firstWord:
            x += str(alphabet[w])
        
        
        for w in secondWord:
            y += str(alphabet[w])
        
        for w in targetWord:
            z += str(alphabet[w])

        print(x, y, z)
        

        return int(z) == int(x)+int(y)