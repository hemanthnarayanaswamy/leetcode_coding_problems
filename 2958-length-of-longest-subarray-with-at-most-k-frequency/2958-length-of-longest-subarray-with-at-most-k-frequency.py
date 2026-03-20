class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        res = 0

        for right in range(len(nums)):
            num = nums[right]
            freq[num] += 1

            while freq[num] > k:
                x = nums[left]
                freq[x] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res