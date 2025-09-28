class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
         # inequality triangle a + b > c, a + c > b, and b + c > a.

        # sort list in descending order 
        nums.sort(reverse=True) ## REversing the sorting order to make it easier
        # print(nums)

        for i in range(len(nums) - 2): ## using range normally will help 
        # if meets condition (a+b > c), then return sum
            if nums[i] < nums[i + 1] + nums[i + 2]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        # else return 0;
        return 0