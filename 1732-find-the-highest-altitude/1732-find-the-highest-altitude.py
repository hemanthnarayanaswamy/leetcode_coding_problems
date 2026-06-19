class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAlt = alt = 0

        for g in gain:
            alt += g 
            
            if alt > maxAlt:
                maxAlt = alt
        
        return maxAlt
