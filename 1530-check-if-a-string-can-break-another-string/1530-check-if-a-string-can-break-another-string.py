class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        s2 = sorted(s2)

        BreakFlag = True

        for i in range(len(s1)):
            if ord(s1[i]) >= ord(s2[i]):
                continue
            else:
                BreakFlag = False
                break
        
        if BreakFlag == True:
            return BreakFlag
        else:
            for i in range(len(s1)):
                if ord(s2[i]) >= ord(s1[i]):
                    continue
                else:
                    BreakFlag = True
                    break

        return not BreakFlag