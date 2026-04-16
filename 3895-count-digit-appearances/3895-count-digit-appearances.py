class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        s=0
        digit=str(digit)
        for i in nums:
            s+=str(i).count(digit)
        return s
        