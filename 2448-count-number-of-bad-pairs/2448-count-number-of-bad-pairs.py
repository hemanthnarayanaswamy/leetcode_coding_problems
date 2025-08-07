class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        totalPairs_count = n*(n-1) // 2
        goodPairsFreq = {}
        goodPair_count = 0

        for i, num in enumerate(nums):
            x = num - i
            goodPairsFreq[x] = goodPairsFreq.get(x, 0) + 1
        
        for _, v in goodPairsFreq.items():
            goodPair_count += v * (v-1) // 2

        return totalPairs_count - goodPair_count
        