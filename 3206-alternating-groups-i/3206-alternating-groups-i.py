class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        groupCount = 0

        for i in range(n):
            if colors[i] != colors[(i+1)%n] != colors[(i+2)%n]:
                groupCount += 1
        
        return groupCount