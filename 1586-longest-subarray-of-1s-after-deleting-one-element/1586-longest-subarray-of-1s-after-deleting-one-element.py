class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = [0] * len(nums)
        numsFreq = Counter(nums)

        if numsFreq.get(0, 0) == 0:
            return len(nums) - 1
        elif numsFreq.get(1, 0) == 0:
            return 0 

        count1 = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count1 += 1
            else:
                res[i] += count1
                count1 = 0
        
        count1 = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 1:
                count1 += 1
            else:
                res[i] += count1
                count1 = 0
        
        return max(res)