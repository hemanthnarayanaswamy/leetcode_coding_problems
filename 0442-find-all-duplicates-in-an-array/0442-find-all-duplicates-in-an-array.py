class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        unique = set()
        for num in nums:
            if num in unique:
                result.append(num)
            else:
                unique.add(num)
        return result
        