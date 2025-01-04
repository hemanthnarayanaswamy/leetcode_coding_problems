class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return nums + nums

## Its better solution
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]: ## Time Complexity O(n)
        return nums * 2  # Repeat the list twice
