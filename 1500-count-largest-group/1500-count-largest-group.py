class Solution:
    def countLargestGroup(self, n: int) -> int:
        numGroup = {}

        for i in range(1, n+1):
            temp = sum([int(j) for j in str(i)])
            numGroup[temp] = numGroup.get(temp, 0) + 1
        
        groupSize = [v for v in numGroup.values()]
        
        return groupSize.count(max(groupSize)) 






