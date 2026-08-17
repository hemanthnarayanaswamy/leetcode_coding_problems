class Solution:
    def minPenalty(self, period: int, lights: list[int], arrivalTime: list[int]) -> int:
        ma = max(lights)
        mi = min(lights)
        penalty = 0

        for t in arrivalTime:
            r = t % period

            if r >= ma:
                penalty = max(penalty, period - r)
        
        return penalty