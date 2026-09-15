class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        dist = 0

        while mainTank>=5:
            mainTank -= 5
            dist += 50

            if additionalTank:
                mainTank += 1
                additionalTank -= 1    

        dist += mainTank*10 
        return dist