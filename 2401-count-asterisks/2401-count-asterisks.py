class Solution:
    def countAsterisks(self, s: str) -> int:
        s = s.split('|')
        result = 0

        for i in range(0, len(s), 2):
            result += s[i].count('*')
        
        return result
