class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        distance_covered = 0

        for point in gain: 
            distance_covered += point 
            if distance_covered > max_altitude:
                max_altitude = distance_covered
        
        return max_altitude
        