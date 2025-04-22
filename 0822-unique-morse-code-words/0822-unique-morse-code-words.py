class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        unqCode = set() 
        codes = {'a':".-", 'b':"-...", 'c':"-.-.", 'd':"-..", 'e':".", 'f':"..-.", 'g':"--.", 'h':"....", 'i':"..", 'j':".---", 'k':"-.-", 'l':".-..", 'm':"--", 'n':"-.", 'o':"---", 'p':".--.", 'q':"--.-", 'r':".-.", 's':"...", 't':"-", 'u':"..-", 'v':"...-", 'w':".--", 'x':"-..-", 'y':"-.--", 'z':"--.."}

        for word in words:
            temp = ''
            for letter in word:
                temp += codes[letter]
            
            unqCode.add(temp)
        
        return len(unqCode)
        