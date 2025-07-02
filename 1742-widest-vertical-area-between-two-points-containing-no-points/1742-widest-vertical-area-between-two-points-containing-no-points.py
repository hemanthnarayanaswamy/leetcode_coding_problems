class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        xs = [p[0] for p in points]

        xs.sort()

        max_width = 0
        for i in range(1, len(xs)):
            width = xs[i] - xs[i - 1]
            if width > max_width:
                max_width = width

        return max_width
            