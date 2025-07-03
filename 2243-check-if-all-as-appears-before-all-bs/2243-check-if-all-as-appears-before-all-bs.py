class Solution:
    def checkString(self, s: str) -> bool:
        seenB = False 

        for c in s:
            if c == 'b':
                seenB = True
            elif seenB: # check c == a after already seen b
                return False
        
        return True