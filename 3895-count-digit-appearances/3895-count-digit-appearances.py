class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        def countDict(num):
            count = 0
            while num:
                q, r = divmod(num, 10)
                num = q
                if r == digit:
                    count += 1
            return count
        
        total = 0 
        
        for num in nums:
            total += countDict(num)
        
        return total

