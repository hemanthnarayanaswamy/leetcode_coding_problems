class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        N = len(nums)
        maxLeft = minLeft = nums[0]

        # Start off being at least m-1 distance apart (this gives subsequence of size m)
        max_product = -inf
        for idx in range(m-1, N):
            rightVal = nums[idx]

            # Check to see if there are new updates to maxLeft and minLeft
            maxLeft = max(maxLeft, nums[idx+1-m])
            minLeft = min(minLeft, nums[idx+1-m])

            # Check to see if there is a new max product
            max_product = max(max_product, rightVal * maxLeft, rightVal * minLeft)

        return max_product