class Solution:
    def minMoves(self, nums: List[int]) -> int:
        minValue = min(nums)
        moves = 0

        for num in nums:
            moves += abs(num - minValue)
        
        return moves
        