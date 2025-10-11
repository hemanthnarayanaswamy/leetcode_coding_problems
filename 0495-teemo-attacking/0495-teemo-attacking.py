class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        attackTime = duration

        for i in range(len(timeSeries)-1):
            tmp = timeSeries[i] + duration
            if tmp < timeSeries[i+1]:
                attackTime += duration
            else:
                attackTime += (timeSeries[i+1] - timeSeries[i])
        
        return attackTime