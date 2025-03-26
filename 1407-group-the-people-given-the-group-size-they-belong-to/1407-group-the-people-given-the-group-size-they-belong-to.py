class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = {}
        groups = []
        
        for i in range(len(groupSizes)):
            if groupSizes[i] not in result:
                result[groupSizes[i]] = [i]
            else:
                result[groupSizes[i]].append(i)

        for size, people in result.items():
            for i in range(0, len(people), size):
                groups.append(people[i:i + size])
        
        return groups
        