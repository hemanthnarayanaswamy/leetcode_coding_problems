class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        results = {}

        for index,num in enumerate(nums):
            diff = target - num
            if diff in results:
                return [index, results[diff]]
            
            results[num] = index
        return none