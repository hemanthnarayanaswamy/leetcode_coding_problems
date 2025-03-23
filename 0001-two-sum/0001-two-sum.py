class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        results = {} 

        for index,num in enumerate(nums):
            diff = target - num
            if diff in results:
                return [index, results[diff]]
            
            results[num] = index
        return none
        