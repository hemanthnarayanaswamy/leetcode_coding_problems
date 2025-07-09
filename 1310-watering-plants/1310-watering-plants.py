class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        capacityLeft = capacity 
        totalSteps = 0

        for i in range(len(plants)):
            totalSteps += 1
            if capacityLeft < plants[i]:
                totalSteps += 2*(i)
                capacityLeft = capacity - plants[i]
            else:
                capacityLeft -= plants[i]
        
        return totalSteps

                