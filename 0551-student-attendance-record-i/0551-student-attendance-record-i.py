class Solution:
    def checkRecord(self, s: str) -> bool:
        absentCount = lateCount = 0

        for d in s:
            if d == 'A':
                absentCount += 1
                lateCount = 0
                if absentCount == 2:
                    return False
            elif d == 'L':
                lateCount += 1
                if lateCount == 3:
                    return False
            else:
                lateCount = 0
        
        return True
