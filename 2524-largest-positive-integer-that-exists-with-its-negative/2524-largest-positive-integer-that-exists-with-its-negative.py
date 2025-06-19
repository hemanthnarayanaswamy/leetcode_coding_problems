class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        larNum = -1 

        numsUniq = set(nums)

        for num in numsUniq:
            if -num in numsUniq and abs(num) > larNum:
                larNum = abs(num)
        
        return larNum

            