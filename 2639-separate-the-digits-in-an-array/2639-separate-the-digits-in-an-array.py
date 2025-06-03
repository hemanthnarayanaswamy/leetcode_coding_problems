class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        numStr = ''.join([str(num) for num in nums])

        return [int(i) for i in numStr]