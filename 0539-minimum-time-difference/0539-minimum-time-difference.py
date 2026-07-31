class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []

        for t in timePoints:
            h, m = t.split(':')
            minutes.append(int(h)*60+int(m))
 
        minutes.sort()

        minDiff = float('inf')

        for i in range(1, len(minutes)):
            minDiff = min(minDiff, minutes[i]-minutes[i-1])
        
        return min(minDiff, 24*60 - minutes[-1]+minutes[0])
    