class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        numsFreq = Counter(nums)
        count, maxNum = 0, 0

        for v in numsFreq.values():
            if v > maxNum:
                maxNum = v
                count = 1
            elif v == maxNum:
                count += 1
        
        return count*maxNum

        