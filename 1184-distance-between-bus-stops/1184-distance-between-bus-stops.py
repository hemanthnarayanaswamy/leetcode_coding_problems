class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:

        total=sum(distance)
        direct=0
        l=min(start,destination)
        r=max(start,destination)
        while l<r:
            direct+=distance[l]
            l+=1
        return min(direct,total-direct)
        