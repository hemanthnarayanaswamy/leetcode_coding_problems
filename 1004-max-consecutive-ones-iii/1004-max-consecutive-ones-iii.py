class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int: 
        maxCount = 0
        freq = defaultdict(int)
        left = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1

            while freq[0] > k:
                freq[nums[left]] -= 1
                left += 1
            
            maxCount = max(maxCount, freq[0]+freq[1])
       
        return maxCount