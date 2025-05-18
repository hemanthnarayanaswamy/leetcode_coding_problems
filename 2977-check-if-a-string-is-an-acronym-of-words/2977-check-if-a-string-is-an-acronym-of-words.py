class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(s) != len(words):
            return False
        
        for i in range(len(s)):
            # if not words[i].startswith(s[i]):
            if words[i][0] != s[i]:
                return False 
        
        return True