class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        start, end = rounds[0], rounds[-1]

        if start <= end:
            return [i for i in range(start, end+1)]
        
        res = []

        for i in range(1, end+1):
            res.append(i)

        for j in range(start, n+1):
            res.append(j)
        
        return res
    