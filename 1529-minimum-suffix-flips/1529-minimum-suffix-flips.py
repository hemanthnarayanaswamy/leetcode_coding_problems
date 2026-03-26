class Solution:
    def minFlips(self, target: str) -> int:
        n = len(target)
        current = '0'
        flips = 0

        for i in range(n):
            if target[i] != current:
                flips += 1
                current = '1' if current == '0' else '0'
        
        return flips
