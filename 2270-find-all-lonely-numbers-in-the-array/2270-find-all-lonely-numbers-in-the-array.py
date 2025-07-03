class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        res = []

        numsFreq = Counter(nums)

        for num in numsFreq:
            if numsFreq[num] == 1:
                if num + 1 not in numsFreq and num - 1 not in numsFreq:
                    res.append(num)
        
        return res