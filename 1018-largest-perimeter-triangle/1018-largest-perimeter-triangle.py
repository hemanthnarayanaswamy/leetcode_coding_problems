class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        if len(nums) < 3: ## If the given lengths are less than 3 sides return 0
            return 0
    
        nums.sort() ## sorting the array 
        print(nums)

        for i in range(len(nums)-1, -1, -1): ## We are starting from the largest side
            print(nums[i], nums[i-1], nums[i-2])
            if i-2 >= 0 and  nums[i] < nums[i-1] + nums[i-2]:
                return nums[i] + nums[i-1] + nums[i-2]
        return 0

        