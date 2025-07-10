class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        slist = list(s)
        n = len(s)

        while n:
            slist.append(slist.pop(0))

            if ''.join(slist) == goal:
                return True 
            
            n -= 1
        
        return False 