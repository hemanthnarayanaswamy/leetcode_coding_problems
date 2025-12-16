class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remainingCapacity = []
        fullBags = 0

        for c,r in zip(capacity, rocks):
            if c == r:
                fullBags += 1
            else:
                remainingCapacity.append(c-r)

        spaceAvailable = sum(remainingCapacity)

        if(additionalRocks  >= spaceAvailable):
            fullBags += len(remainingCapacity)
            return fullBags

        remainingCapacity.sort()
        

        for cap in remainingCapacity:
            if cap <= additionalRocks:
                fullBags += 1
                additionalRocks -= cap
                if not additionalRocks:
                    break
        
        return fullBags