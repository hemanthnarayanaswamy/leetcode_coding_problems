class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        numsU = set(nums)

        for num in nums:
            y = num + diff
            z = num + 2*diff 

            if y in numsU and z in numsU:
                count += 1
        
        return count