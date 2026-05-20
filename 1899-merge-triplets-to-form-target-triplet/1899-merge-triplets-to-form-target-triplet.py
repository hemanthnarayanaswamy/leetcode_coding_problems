class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target[0], target[1], target[2]
        freq = {x: 0, y: 0, z: 0}

        for a, b, c in triplets:
            if a <= x and b <= y and c <= z:
                if a == x:
                    freq[x] += 1
            
                if b == y:
                    freq[y] += 1
                
                if c == z:
                    freq[z] += 1
        
        for v in freq.values():
            if v == 0:
                return False
        
        return True