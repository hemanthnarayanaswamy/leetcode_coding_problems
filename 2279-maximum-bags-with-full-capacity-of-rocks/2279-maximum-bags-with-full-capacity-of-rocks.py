class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remainingCapacity = [c-r for c,r in zip(capacity, rocks)]
        spaceAvailable = sum(remainingCapacity)

        if(additionalRocks  >= spaceAvailable):
            return len(remainingCapacity)

        remainingCapacity.sort()
        fullBags = 0

        for cap in remainingCapacity:
            if cap == 0:
                fullBags += 1
            elif cap <= additionalRocks:
                fullBags += 1
                additionalRocks -= cap
                if not additionalRocks:
                    break
        
        return fullBags