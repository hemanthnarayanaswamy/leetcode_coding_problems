class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        numsFreq = Counter(nums)
        sortedFreq = sorted(numsFreq.items(), key=lambda x: (x[1], -x[0]))

        result = []
        for num, count in sortedFreq:
            result.extend([num] * count)
            
        return result