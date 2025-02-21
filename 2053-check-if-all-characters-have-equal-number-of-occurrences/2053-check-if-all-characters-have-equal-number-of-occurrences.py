class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        char_freq = Counter(s) ## To get the frequenccy of elements 
        result = 0 ## To store individual occurances

        for char in char_freq:
            if result == 0:
                result = char_freq[char] ## Assign the result with the first occurrence value
            else:
                if result != char_freq[char]: # Retur false if the count is off
                    return False

        return True
        