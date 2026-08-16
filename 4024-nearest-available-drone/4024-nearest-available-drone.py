class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        x, y = target
        res = -1
        dist = float('inf')

        for i, drone in enumerate(drones):
            x2, y2, r = drone

            m = abs(x - x2) + abs(y - y2)

            if m <= r:
                if m < dist:
                    dist = m
                    res = i
        
        return res
