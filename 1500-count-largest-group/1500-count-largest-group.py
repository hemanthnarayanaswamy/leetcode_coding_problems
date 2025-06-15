class Solution:
    def countLargestGroup(self, n: int) -> int:
        numGroup = {}
        maxGroupSize = 0
        count = 0

        for i in range(1, n+1):
            if i < 9:
                numGroup[i] = numGroup.get(i, 0) + 1
            else:
                temp = sum([int(j) for j in str(i)])
                numGroup[temp] = numGroup.get(temp, 0) + 1

        for v in numGroup.values():
            if v > maxGroupSize:
                maxGroupSize = v
                count = 0

            if v == maxGroupSize:
                count += 1
        
        return count






