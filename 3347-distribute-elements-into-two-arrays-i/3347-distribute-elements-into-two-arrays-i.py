class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n == 1:
            return nums

        arr1, arr2 = [nums[0]], [nums[1]]

        i = 2

        while i < n:
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
            i += 1
        
        return arr1 + arr2
