class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])
        result = [[0] * cols for _ in range(rows)]

        def get_average(row, col):
            row_start = max(0, row - 1)
            row_end = min(rows, row + 1)

            col_start = max(0, col - 1)
            col_end = min(cols, col + 1)

            total = 0
            points = 0

            for current_row in img[row_start:row_end+1]:
                neighbors = current_row[col_start:col_end+1]

                total += sum(neighbors)
                points += len(neighbors)

            return total // points

        for row in range(rows):
            for col in range(cols):
                result[row][col] = get_average(row, col)

        return result