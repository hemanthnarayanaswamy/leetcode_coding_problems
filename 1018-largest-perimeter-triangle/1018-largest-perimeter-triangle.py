class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # if nums_lenght < 3: ## If the given lengths are less than 3 sides return 0
        #     return 0        ## It is not necessary as it'll be fine 
    
        nums.sort() ## sorting the array 

        for i in range(len(nums)-1, 1, -1): ## We are starting from the largest side
            sum_of_sides = nums[i-1] + nums[i-2]
            largest_side = nums[i]
            if largest_side < sum_of_sides:
                return largest_side + sum_of_sides
        return 0

        