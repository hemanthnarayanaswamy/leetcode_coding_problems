class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        numsFreq = Counter(nums)

        for k, v in numsFreq.items():
            if v == 1:
                return k