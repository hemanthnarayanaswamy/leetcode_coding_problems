class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        ans = 0
        max_pos = 0
        
        for step, pos in enumerate(flips, 1):
            max_pos = max(max_pos, pos)
            if max_pos == step:
                ans += 1
        return ans