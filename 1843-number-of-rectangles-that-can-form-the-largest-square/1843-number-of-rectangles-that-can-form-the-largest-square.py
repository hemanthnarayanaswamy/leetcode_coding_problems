class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        squareSides = {}
        maxLen = 0

        for l, w in rectangles:
            s = min(l, w)
            squareSides[s] = squareSides.get(s, 0) + 1

            if s > maxLen:
                maxLen = s

        return squareSides[maxLen]
