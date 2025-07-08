class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sort based on the units 
        boxTypes = sorted(boxTypes, key=lambda x: int(x[1]), reverse=True) 
        units_total = 0
        
        for b,u in boxTypes:
            if truckSize>=b:
                truckSize-=b
                units_total+=b*u
            else:
                units_total+=truckSize*u
                break
        
        return units_total
