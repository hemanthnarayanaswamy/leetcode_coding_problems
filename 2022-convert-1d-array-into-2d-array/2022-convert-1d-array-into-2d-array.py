class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        result = []
        idx = 0
        if m * n == len(original):
            for i in range(m):
                result.append(original[idx:idx+n])
                idx += n
        
        return result
