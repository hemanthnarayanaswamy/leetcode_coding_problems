class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        clockWiseDistance = anticlockWiseDistance = 0
        n = len(distance)

        if start > destination:
            start, destination = destination, start

        for i in range(start, destination):
            clockWiseDistance += distance[i]

        anticlockWiseDistance = sum(distance) - clockWiseDistance
        
        return clockWiseDistance if clockWiseDistance < anticlockWiseDistance else anticlockWiseDistance
