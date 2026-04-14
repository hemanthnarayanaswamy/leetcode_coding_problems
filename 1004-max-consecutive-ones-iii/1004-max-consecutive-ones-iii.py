class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int: 
        maxCount = 0
        freq = [0, 0]
        left = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1

            while freq[0] > k:
                freq[nums[left]] -= 1
                left += 1
            
            maxCount = max(maxCount, sum(freq))
       
        return maxCount