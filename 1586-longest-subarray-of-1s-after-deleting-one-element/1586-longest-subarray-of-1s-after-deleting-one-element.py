class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        leftOnes = [0] * len(nums)
        rightOnes = [0] * len(nums)

        numsFreq = Counter(nums)

        count1 = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count1 += 1
            else:
                leftOnes[i] = count1
                count1 = 0
        
        count1 = 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 1:
                count1 += 1
            else:
                rightOnes[i] = count1
                count1 = 0
        
        longestLen = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                tmp = leftOnes[i] + rightOnes[i]
                if tmp > longestLen:
                    longestLen = tmp
        
        if numsFreq.get(0, 0) == 0:
            return len(nums) - 1
        elif numsFreq.get(1, 0) == 0:
            return 0
        else:
            return longestLen
