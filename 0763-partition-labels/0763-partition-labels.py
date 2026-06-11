class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end_idx = defaultdict(int)

        for i, ch in enumerate(s):
            end_idx[ch] = i
        
        res = []
        start = end = 0

        for i, ch in enumerate(s):
            end = max(end, end_idx[ch])

            if i == end:
                res.append(end - start + 1)
                start = i + 1

        return res