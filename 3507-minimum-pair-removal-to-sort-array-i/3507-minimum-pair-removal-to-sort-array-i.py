class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        moves = 0

        if len(nums) < 2:
            return moves

        def check_sorted(nums):
            return nums == sorted(nums)
        
        def replacePair(nums, i1, i2):
            new = nums[:i1] + [sum(nums[i1:i2+1])] + nums[i2+1:]
            return new
        
        while not check_sorted(nums):
            minSum = float('inf')
            i1 = i2 = None

            for i in range(1, len(nums)):
                p, c = nums[i-1], nums[i]
                tmp = p+c
                if tmp < minSum:
                    minSum = tmp
                    i1 = i-1
                    i2 = i

            nums = replacePair(nums, i1, i2)
            moves += 1
        
        return moves
