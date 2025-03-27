class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_freq = Counter(ransomNote)
        magazine_freq = Counter(magazine)

        for letter in ransomNote_freq:
            if letter not in magazine_freq:
                return False
            if ransomNote_freq[letter] > magazine_freq[letter]:
                return False 
        
        return True 
        