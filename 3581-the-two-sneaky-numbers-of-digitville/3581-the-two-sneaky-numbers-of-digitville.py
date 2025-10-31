class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        numsFreq = Counter(nums)

        return [n for n,v in numsFreq.items() if v == 2]