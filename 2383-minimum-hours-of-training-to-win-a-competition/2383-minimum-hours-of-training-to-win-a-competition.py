class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:    
        totalTime = 0
        totalEnergy = sum(energy)

        if totalEnergy >= initialEnergy:
            energyTrainingTime = (totalEnergy - initialEnergy) + 1
            initialEnergy += energyTrainingTime
            totalTime += energyTrainingTime

        for en, exp in zip(energy, experience):
            if initialExperience <= exp:
                expTrainingTime = exp - initialExperience + 1
                totalTime += expTrainingTime
                initialExperience += (expTrainingTime)

            initialEnergy -= en
            initialExperience += exp
        
        return totalTime