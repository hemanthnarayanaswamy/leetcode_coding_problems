class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = 0, 1
        while even < len(nums)-1 and odd < len(nums):
            if nums[even] % 2 == 0 and nums[odd] % 2 == 1:
                even += 2
                odd += 2
            elif nums[even] % 2 != 0 and nums[odd] % 2 != 1:
                nums[even], nums[odd] = nums[odd], nums[even]
                even += 2
                odd += 2
            else:
                if nums[even] % 2 != 0:
                    odd += 2
                else:
                    even += 2
        
        return nums
        