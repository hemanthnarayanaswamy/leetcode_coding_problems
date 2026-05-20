class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)

        def checkValidity(t):
            for x, y in zip(target, t):
                if x < y:
                    return False
            return True

        valid = []
        for t in triplets:
            if checkValidity(t):
                valid.append(t)
        
        if valid and target in valid:
                return True

        if len(valid) < 2:
            return False

        x, y, z = target[0], target[1], target[2]
        freq = {x: 0, y: 0, z: 0}

        for a,b,c in valid:
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