class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        numsFreq = Counter(nums)
        res = []

        for num in numsFreq:
            if numsFreq[num] == 1:
                res.append(num)
            
            if len(res) == 2:
                return res
