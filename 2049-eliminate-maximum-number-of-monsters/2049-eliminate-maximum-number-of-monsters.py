class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        time_taken = sorted([dist[i]/speed[i] for i in range(n)])
        # time_taken = sorted([d/s for d, s in zip(dist, speed)])
        
        for i in range(n):
            if time_taken[i] <= i:
                return i
        return n

            