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
        
        boats += len(people[r+1:])
        print()

        while l <= r:
            if people[l] + people[r] <= limit:
                boats += 1
                l += 1
                r -= 1
            else:
                boats += 1
                r -= 1
        
        return boats