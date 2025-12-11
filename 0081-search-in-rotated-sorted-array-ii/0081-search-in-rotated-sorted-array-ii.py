class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        numsFreq = Counter(nums)

        return target in numsFreq