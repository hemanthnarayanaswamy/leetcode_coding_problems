class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        count = 0
        
        for i in range(n):
            prev = colors[(i - 1) % n]
            curr = colors[i]
            nxt = colors[(i + 1) % n]
            
            if curr != prev and curr != nxt:
                count += 1
                
        return count  