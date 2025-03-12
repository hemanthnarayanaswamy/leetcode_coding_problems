class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_altitude = 0
        distance_covered = 0

        for point in gain: 
            distance_covered += point 
            max_altitude = max(distance_covered, max_altitude)
        
        return max_altitude
        