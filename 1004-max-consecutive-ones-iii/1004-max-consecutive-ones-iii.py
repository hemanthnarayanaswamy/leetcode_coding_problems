class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int: 
        numsFreq = Counter(nums)
        maxCount = count = 0
        freq = defaultdict(int)
        left = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1

            while freq[0] > k:
                freq[nums[left]] -= 1
                left += 1
            
            count = freq[1]
            if count > maxCount:
                maxCount = count
        
        if k > numsFreq[0]:
            total = maxCount + numsFreq[0]
        else:
            total = maxCount + k

        return total