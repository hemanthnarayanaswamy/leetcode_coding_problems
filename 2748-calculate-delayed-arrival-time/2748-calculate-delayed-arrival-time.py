class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        sum = arrivalTime + delayedTime 

        return sum - 24 if sum >= 24 else sum