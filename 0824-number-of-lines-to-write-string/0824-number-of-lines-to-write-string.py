class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1                  # we’ll need at least one line
        cur   = 0                  # width used on the current line
        wmap  = widths             # local alias—faster than repeated attribute lookups
        base  = ord('a')           # cache this too

        for ch in s:               # direct iteration instead of indexing
            w = wmap[ord(ch) - base]
            # if adding this char would overflow, start a new line
            if cur + w > 100:
                lines += 1
                cur    = w
            else:
                cur   += w

        return [lines, cur]
