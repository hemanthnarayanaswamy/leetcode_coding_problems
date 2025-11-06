class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        lo, hi = s.split(':')
        c1, c2 = ord(lo[0]), ord(hi[0])
        r1, r2 = int(lo[1:]), int(hi[1:])
        return [f"{chr(c)}{r}" for c in range(c1, c2 + 1) for r in range(r1, r2 + 1)]