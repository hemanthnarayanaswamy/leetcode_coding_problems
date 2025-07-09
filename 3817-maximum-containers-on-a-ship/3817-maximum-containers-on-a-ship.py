class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        cargoCells = n * n 
        possibleContainers = maxWeight // w 

        return min(cargoCells, possibleContainers)
