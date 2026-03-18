class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[:k-1])
        start = 0
        i = 1
        res = 0

        while i < len(colors):
            if colors[i] != colors[i-1]:
                if i - start + 1 >= k:
                    res += 1
            else:
                start = i
            i += 1
        
        return res

