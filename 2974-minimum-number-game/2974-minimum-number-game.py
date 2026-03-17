class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []

        # nums is sorted ascending, so smallest elements are at the front
        # We take them in pairs and swap them
        for i in range(0, len(nums), 2):
            res.append(nums[i+1])
            res.append(nums[i])

        return res