class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        result = [0]*n
        track_index = set()
        

        for i in range(n):
            if s[i] == c:
                track_index.add(i)
        
        for i in range(n):
            if s[i] == c:
                continue
            diff_val = min(abs(i - x) for x in track_index)
            result[i] = diff_val

        return result
        