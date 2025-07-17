class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        oddSort = []
        evenSort = []
        result = []

        for i in range(len(nums)):
            if i % 2:
                oddSort.append(nums[i])
            else:
                evenSort.append(nums[i])
        
        oddSort.sort(reverse=True)
        evenSort.sort()

        for i in range(len(oddSort)):
            result.append(evenSort[i])
            result.append(oddSort[i])
        
        if len(result) == len(nums):
            return result 
        else:
            result.append(evenSort[-1])

        return result
