class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counts = Counter(map(tuple, grid))
        answer = 0

        for col in list(zip(*grid)):
            answer += row_counts[col]
        
        return answer
