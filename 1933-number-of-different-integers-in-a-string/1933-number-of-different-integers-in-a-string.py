class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        digit_index = 0
        digit_found = False
        number_list = set()
        
        for i in range(len(word)):
            if word[i].isdigit() and not digit_found: 
                digit_index = i 
                digit_found = True

            if not word[i].isdigit() and digit_found: 
                number_list.add(int(word[digit_index:i]))
                digit_found = False

            if i == len(word) -1 and digit_found: 
                number_list.add(int(word[digit_index:i+1])) 

        return len(number_list) 