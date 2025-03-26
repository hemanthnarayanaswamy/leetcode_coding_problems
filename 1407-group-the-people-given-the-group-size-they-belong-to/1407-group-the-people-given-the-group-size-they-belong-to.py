class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = defaultdict(list)
        groups = []
        
        for i, size in enumerate(groupSizes):
            result[size].append(i)

        for size, people in result.items():
            for i in range(0, len(people), size):
                groups.append(people[i:i + size])
        
        return groups
        