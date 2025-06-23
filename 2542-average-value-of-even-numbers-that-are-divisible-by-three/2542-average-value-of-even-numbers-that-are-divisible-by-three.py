class Solution:
    def averageValue(self, nums: List[int]) -> int:
        avgsum  = []

        for num in nums:
            if num % 2 == 0 and num % 3 == 0: 
                avgsum.append(num)

        return sum(avgsum) // len(avgsum) if avgsum else 0

