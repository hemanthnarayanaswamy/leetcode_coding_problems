class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        totalLines, maxWidth = 1, 0

        for i in range(len(s)):
            charWidth = widths[ord(s[i]) - 97]
            if maxWidth + charWidth > 100:
                totalLines += 1
                maxWidth = charWidth
            else:
                maxWidth += charWidth
        
        return [totalLines, maxWidth]