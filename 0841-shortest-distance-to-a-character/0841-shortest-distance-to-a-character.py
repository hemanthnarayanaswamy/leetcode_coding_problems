class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        result = []
        track_index = set()

        for i in range(len(s)):
            if s[i] == c:
                track_index.add(i)
        
        for i in range(len(s)):
            diff_val = min(abs(i - x) for x in track_index)
            result.append(diff_val)

        return result
        