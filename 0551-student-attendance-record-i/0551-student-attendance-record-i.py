class Solution:
    def checkRecord(self, s: str) -> bool:
        absentCount = lateCount = 0

        for d in s:
            if d == 'A':
                absentCount += 1
                lateCount = 0
            elif d == 'L':
                lateCount += 1
            else:
                lateCount = 0
            
            if absentCount == 2 or lateCount == 3:
                return False
        
        return True