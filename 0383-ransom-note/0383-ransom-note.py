class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_freq = Counter(ransomNote)

        for letter in ransomNote_freq:
            if ransomNote_freq[letter] > magazine.count(letter):
                return False 
        
        return True 
        