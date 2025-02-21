class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        # if len(s) % 2 != 0: ## Not required as 
        #     return False   ## Fail for s = "vvvvvvvvvvvvvvvvvvv"
    
        char_freq = Counter(s)
        result = set()

        for char in char_freq:
            result.add(char_freq[char]) 

        return True if len(result) == 1 else False
        