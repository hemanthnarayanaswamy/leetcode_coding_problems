class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        descentDays = 0
        contiguousDays = 1

        for i in range(1, len(prices)):
            if prices[i] == prices[i-1]-1:
                contiguousDays += 1
            else:
                descentDays += (contiguousDays*(contiguousDays+1)) // 2
                contiguousDays = 1
        
        descentDays += (contiguousDays*(contiguousDays+1)) // 2

        return descentDays
