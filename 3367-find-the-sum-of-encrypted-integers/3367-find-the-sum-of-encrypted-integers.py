class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        total = 0
        for n in nums:
            s = str(n)
            # largest character in the string, still a string
            m = max(s)        
            # repeat it len(s) times, then parse
            total += int(m * len(s))
        return total
