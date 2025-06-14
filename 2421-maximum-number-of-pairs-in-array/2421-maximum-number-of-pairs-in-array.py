class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        numPairs, leftOver = 0, 0 
        numsFreq = Counter(nums)

        for val in numsFreq.values():
            numPairs += val // 2
            leftOver += val % 2
        
        return [numPairs, leftOver]