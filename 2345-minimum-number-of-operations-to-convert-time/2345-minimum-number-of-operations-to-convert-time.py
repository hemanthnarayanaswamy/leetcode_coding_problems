class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        current_minutes = int(current[:2])*60 + int(current[3:])
        corrent_minutes = int(correct[:2])*60 + int(correct[3:])

        totalDiff = corrent_minutes - current_minutes
        totalOperations = 0

        while totalDiff != 0:
            if totalDiff >= 60:
                totalDiff -= 60
            elif 15 <= totalDiff < 60:
                totalDiff -= 15
            elif 5 <= totalDiff < 15:
                totalDiff -= 5
            else:
                totalDiff -= 1
            
            totalOperations += 1

        return totalOperations


