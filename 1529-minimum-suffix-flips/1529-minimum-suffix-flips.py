class Solution:
    def minFlips(self, target: str) -> int:
        current = '0'
        flips = 0

        for b in target:
            if b != current:
                flips += 1
                current = b
        
        return flips
