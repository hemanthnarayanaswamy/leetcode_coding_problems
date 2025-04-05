class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_idx = 0 
        negative_idx = 1
        result = [0]*len(nums)

        for num in nums:
            if num >= 0:
                result[positive_idx] = num
                positive_idx += 2
            else:
                result[negative_idx] = num
                negative_idx += 2

        return result