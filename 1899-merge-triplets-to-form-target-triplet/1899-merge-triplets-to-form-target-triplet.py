class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        max_a = max_b = max_c = 0
        x, y, z = target[0], target[1], target[2]

        for a, b, c in triplets:  
            if a > x or b > y or c > z: 
                continue
            max_a = max(max_a, a)
            max_b = max(max_b, b)
            max_c = max(max_c, c)
            if max_a == x and max_b == y and max_c == z: 
                return True
                
        return False

