class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time_taken = sorted([dist[i]/speed[i] for i in range(len(dist))])
        # time_taken = sorted([d/s for d, s in zip(dist, speed)])
        
        for i in range(len(time_taken)):
            if time_taken[i] <= i:
                return i
        return len(time_taken)

            