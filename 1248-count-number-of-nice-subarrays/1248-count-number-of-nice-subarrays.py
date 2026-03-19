class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        preOdd = 0
        preFreq = defaultdict(int)
        subCount = 0

        for num in nums:
            if num % 2:
                preOdd += 1
            
            if preOdd == k:
                subCount += 1
            
            subCount += preFreq[preOdd - k]
            preFreq[preOdd] += 1
        
        return subCount