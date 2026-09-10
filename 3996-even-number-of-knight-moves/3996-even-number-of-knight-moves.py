class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        if (start[0] % 2 == start[1] % 2) and (target[0] % 2 == target[1] % 2):
            return True
        
        if (start[0] % 2 != start[1] % 2) and (target[0] % 2 != target[1] % 2):
            return True
        
        return False