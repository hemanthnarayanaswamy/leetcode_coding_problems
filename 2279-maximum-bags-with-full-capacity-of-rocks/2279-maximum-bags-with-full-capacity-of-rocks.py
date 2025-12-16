class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remainingCapacity = [c-r for c,r in zip(capacity, rocks)]
        remainingCapacity.sort()

        fullBags = 0

        for i in range(len(remainingCapacity)):
            if remainingCapacity[i] and remainingCapacity[i] <= additionalRocks:
                additionalRocks -= remainingCapacity[i]
                remainingCapacity[i] = 0
            
            if remainingCapacity[i] == 0:
                fullBags += 1
            
            if additionalRocks == 0:
                break

        return fullBags