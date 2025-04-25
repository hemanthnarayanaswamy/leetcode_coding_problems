class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_sorted = sorted(nums)
        tempMap = {}
        
        n = len(nums)

        for i,num in enumerate(nums_sorted): 
            if num not in tempMap:
                tempMap[num] = i 
    

        result = [0]*len(nums)

        for i in range(n):
            result[i] = tempMap[nums[i]]
        
        return result
        
