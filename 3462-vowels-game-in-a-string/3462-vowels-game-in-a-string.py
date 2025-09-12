class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set('aeiou')
        count = sum([1 for c in s if c in vowels])

        if count == 0:
            return False
        else:
            return True
            
