class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even, odd = 0, 1

        while even < len(nums)-1 and odd < len(nums):

            evenIdx, oddIdx = nums[even]%2, nums[odd]%2
            
            if evenIdx == 0:
                if oddIdx == 1:
                    even += 2
                    odd += 2
                else:
                    even += 2
            else: 
                if oddIdx == 1:
                    odd += 2
                else:
                    nums[even], nums[odd] = nums[odd], nums[even]
                    even += 2
                    odd += 2

        return nums






           
        
      
        