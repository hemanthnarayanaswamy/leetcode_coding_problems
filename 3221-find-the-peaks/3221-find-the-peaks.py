class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []

        i = 1

        while i < len(mountain) - 1:
            p, c, n = mountain[i-1], mountain[i], mountain[i+1]

            if c > p and c > n:
                peaks.append(i)
                i += 2
            else:
                i += 1
        
        return peaks


