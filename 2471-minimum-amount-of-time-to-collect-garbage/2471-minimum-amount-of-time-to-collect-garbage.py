class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # Step 1: Build prefix sum for travel
        n = len(garbage)
        travel_prefix = [0] * n
        for i in range(1, n):
            travel_prefix[i] = travel_prefix[i-1] + travel[i-1]
        
        total_pickups = {'M': 0, 'P': 0, 'G': 0}
        last_seen = {'M': 0, 'P': 0, 'G': 0}

        # Step 2: Count pickups and record last house for each type
        for i, types_garbage in enumerate(garbage):
            for char in types_garbage:
                total_pickups[char] += 1
                last_seen[char] = i

        # Step 3: Calculate total time
        total_time = 0
        
        for char in ['M', 'P', 'G']:
            if total_pickups[char] > 0:
                total_time += total_pickups[char] + travel_prefix[last_seen[char]]

        return total_time
        