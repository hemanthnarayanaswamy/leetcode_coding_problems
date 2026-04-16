class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        def countDict(num):
            freq = Counter(num)
            count = freq[str(digit)]
            return count
        
        total = 0 
        
        for num in nums:
            total += countDict(str(num))
        
        return total

