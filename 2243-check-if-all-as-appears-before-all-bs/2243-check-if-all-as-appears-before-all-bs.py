class Solution:
    def checkString(self, s: str) -> bool:
        countA = s.count('a')

        for c in s:
            if c == 'b' and countA != 0:
                return False
            elif c == 'a':
                countA -= 1
        
        return True