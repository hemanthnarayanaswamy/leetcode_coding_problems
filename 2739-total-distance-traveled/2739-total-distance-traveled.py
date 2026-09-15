class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        dist = 0

        while mainTank:
            if mainTank >= 5:
                dist += (5*10)
                mainTank -= 5
                if additionalTank:
                    mainTank += 1
                    additionalTank -= 1
            else:
                dist += (mainTank*10)
                mainTank = 0
        
        return dist
