class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, len(nums) - 1

        while l < r:
            x, y = nums[l], nums[r]

            # compute m = 10^(#digits in y)
            m = 1
            while m <= y:
                m *= 10

            # “concatenate” x and y via x*m + y
            res += x * m + y

            l += 1
            r -= 1

        # if there's a middle element (odd length), add it
        if l == r:
            res += nums[l]

        return res
