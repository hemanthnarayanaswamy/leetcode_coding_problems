class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_idx = defaultdict(int)

        for i, ch in enumerate(s):
            end_idx[ch] = i
        
        res = []
        start =  0
        l = r = 0 

        while r < len(s) and l < len(s):
            if l > r:
                res.append(l - start)
                start = l
                r = l
            
            if r < end_idx[s[l]]:
                r = end_idx[s[l]]
            l += 1
        
        res.append(l - start)

        return res


        