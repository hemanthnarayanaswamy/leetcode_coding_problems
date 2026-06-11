class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_idx = defaultdict(int)

        for i, ch in enumerate(s):
            end_idx[ch] = i
        
        res = []
        start = 0
        r = 0

        for l in range(len(s)):
            if l > r:
                res.append(r - start + 1)
                start = l
                r = l
            
            if r < end_idx[s[l]]:
                r = end_idx[s[l]]
        
        res.append(r - start + 1)

        return res