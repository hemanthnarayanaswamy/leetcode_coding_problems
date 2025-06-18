class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:

        lines, total = 1, 0
        L = []
        for c in s:
            total += widths[ord(c) - ord('a')]
            
            if total > 100:
                lines += 1
                total = widths[ord(c) - ord('a')]

        L.append(lines)
        L.append(total)

        return L
       
        