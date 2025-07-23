class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def removeab(tmpLst):
            tmpScore = 0
            stack = []
            for char in tmpLst:
                if stack and char == 'b':
                    if stack[-1] + char == 'ab':
                        tmpScore += x
                        stack.pop()
                    else:
                        stack.append(char)
                else:
                    stack.append(char)

            return tmpScore, stack

        def removeba(tmpLst): 
            tmpScore = 0
            stack = []
            for char in tmpLst:
                if stack and char == 'a':
                    if stack[-1] + char == 'ba':
                        tmpScore += y
                        stack.pop()
                    else:
                        stack.append(char)
                else:
                    stack.append(char)
            
            return tmpScore, stack
        
        tmpLst = s

        if x > y:
            s1, tmpLst = removeab(tmpLst)
            s2, tmpLst = removeba(tmpLst)
        else:
            s1, tmpLst = removeba(tmpLst)
            s2, tmpLst = removeab(tmpLst)
        
        return s1+s2
    
        
