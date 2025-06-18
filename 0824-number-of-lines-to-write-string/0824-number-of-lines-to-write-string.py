class Solution:
    def numberOfLines(self, widths, s):
        max_width = 100
        lines = 1
        current_width = 0

        for ch in s:
            w = widths[ord(ch) - ord('a')]
            if current_width + w > max_width:
                lines += 1
                current_width = w
            else:
                current_width += w

        return [lines, current_width]