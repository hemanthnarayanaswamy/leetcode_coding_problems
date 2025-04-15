class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = s[:spaces[0]]
        for i in range(1, len(spaces)):
            result += ' ' + s[spaces[i-1]:spaces[i]]
        
        return result + ' ' + s[spaces[-1]::]