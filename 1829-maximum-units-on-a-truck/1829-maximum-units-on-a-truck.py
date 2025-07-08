class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sort based on the units 
        boxesSorted = sorted(boxTypes, key=lambda x: int(x[1]), reverse=True) 
        totalUnits = 0
        
        for b, u in boxesSorted:
            if b <= truckSize:
                totalUnits += b * u
                truckSize -= b
            else:
                totalUnits += truckSize * u
                break
        
        return totalUnits
