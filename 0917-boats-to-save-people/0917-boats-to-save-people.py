class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()
        n = len(people)
        l, r = 0, n-1

        for i in range(n):
            if people[i] >= limit:
                r = i - 1
                break 
        # New r idx will be where that person can the paired with min weight person to share a boat
        
        boats += len(people[r+1:]) # Boats for people greater in Weight

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                
            boats += 1
            r -= 1
        
        return boats