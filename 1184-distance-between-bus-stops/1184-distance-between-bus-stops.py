class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        clockWiseDistance = 0

        if start > destination:
            start, destination = destination, start

        for i in range(start, destination):
            clockWiseDistance += distance[i]
        
        return min(clockWiseDistance, sum(distance) - clockWiseDistance)
