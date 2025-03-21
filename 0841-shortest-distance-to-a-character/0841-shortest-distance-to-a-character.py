class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result = []
        track_index = set()
        n = len(s)

        for i in range(n):
            if s[i] == c:
                track_index.add(i)
        
        for i in range(n):
            diff_val = min(abs(i - x) for x in track_index)
            result.append(diff_val)

        return result
        