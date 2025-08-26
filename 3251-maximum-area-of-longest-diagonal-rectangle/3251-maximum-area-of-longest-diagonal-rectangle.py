class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        area = 0
        diagonal = 0

        for l, w in dimensions:
            tmp_diagonal = l*l + w*w
            if tmp_diagonal > diagonal:
                area = l * w
                diagonal = tmp_diagonal
            elif diagonal == tmp_diagonal:
                area = max(area, l * w)

        return area