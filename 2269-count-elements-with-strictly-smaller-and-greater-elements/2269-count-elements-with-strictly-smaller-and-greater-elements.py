class Solution:
    def countElements(self, nums: List[int]) -> int:
        count = 0
        ma, mi = max(nums), min(nums)

        for num in nums:
            if num < ma and num > mi:
                count += 1
        
        return count
