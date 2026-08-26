class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        freq = Counter(nums)

        res = 0

        for k, v in freq.items():
            if v == 2:
                res ^= k
        
        return res