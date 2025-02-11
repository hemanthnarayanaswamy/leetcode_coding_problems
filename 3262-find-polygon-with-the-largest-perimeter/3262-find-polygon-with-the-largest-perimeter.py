class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        len_nums = len(nums)

        nums.sort(reverse=True) ## Sort and reverse the order of the sorted arry to non decresing 

        sum_nums = sum(nums) ## Calculate the over all sum of elements 

        for i in range(len_nums):
            current_edge = nums[i]
            if current_edge < sum_nums - current_edge:
                return sum_nums
            else:
                sum_nums -= current_edge
        return -1
            