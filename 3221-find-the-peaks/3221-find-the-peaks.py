class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []

        for i in range(1, len(mountain)-1):
            p, c, n = mountain[i-1], mountain[i], mountain[i+1]

            if c > p and c > n:
                peaks.append(i)
        
        return peaks