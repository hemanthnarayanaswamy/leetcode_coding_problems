class Solution:
    def minimumChairs(self, s: str) -> int:
        occupied = 0
        chairs = []

        for p in s:
            if p == 'E':
                occupied += 1
            else:
                occupied -= 1
            
            chairs.append(occupied)
        
        return max(chairs)