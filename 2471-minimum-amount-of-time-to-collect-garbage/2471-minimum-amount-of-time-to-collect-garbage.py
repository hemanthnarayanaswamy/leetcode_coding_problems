class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # Step 1: Build prefix sum for travel
        n = len(garbage)

        travel_prefix = [0] * n
        for i in range(1, n):
            travel_prefix[i] = travel_prefix[i-1] + travel[i-1]
        
        travel_prefix = travel_prefix [::-1]
        garbage = garbage[::-1]

        total_time = 0
        M, P, G = 1, 1, 1

        for i in range(n):
            if "M" in garbage[i] and M:
                total_time += travel_prefix[i]
                M = 0
            if "G" in garbage[i] and G:
                total_time += travel_prefix[i]
                G = 0
            if "P" in garbage[i] and P:
                total_time += travel_prefix[i]
                P = 0

            if not(P) and not(G) and not(M):
                break
        
        total_time += len("".join(garbage))

        return total_time