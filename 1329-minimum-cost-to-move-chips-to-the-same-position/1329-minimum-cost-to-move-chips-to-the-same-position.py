class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        chips_even = 0
        chips_odd = 0

        for p in position:
            if p % 2:
                chips_odd += 1
            else:
                chips_even += 1
        
        return min(chips_even, chips_odd)