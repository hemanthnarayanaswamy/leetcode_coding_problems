class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        numsFreq = Counter(nums)

        return sorted(nums, key=lambda x: (numsFreq[x], -x))