class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minValue = min(nums)
        moves = 0

        for num in nums:
            moves += num - minValue
        
        return moves
        