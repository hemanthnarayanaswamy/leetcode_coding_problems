class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = [-1]*len(nums)

        for num, i in zip(nums, index):
            result.insert(i, num)
        
        return [n for n in result if n > -1]
