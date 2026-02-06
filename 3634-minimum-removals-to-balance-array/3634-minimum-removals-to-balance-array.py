class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        moves = float('inf')

        l, r = 0, 1

        while r < n:
            if nums[r] > k * nums[l]:
                moves = min(moves, n - (r - l))
                l += 1
            else:
                r += 1
        
        moves = min(moves, n - (r - l))
        
        return 0 if moves == float('inf') else moves

        