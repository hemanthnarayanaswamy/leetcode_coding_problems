class Solution:
    def mirrorFrequency(self, s: str) -> int:
        freq = Counter(s)
        total = 0
        visited = set()

        for c in freq:
            if c.isnumeric():
                mir = str(9 - int(c))
            else:
                mir = chr(ord('z') - (ord(c) - ord('a')))

            if c not in visited: # If the pair is unique only find the absolute difference
                total += abs(freq[c] - freq[mir]) 
                visited.add(c)
                visited.add(mir)
        
        return total # We need to return the sum of absolute difference of all unique pairs
            