class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefixFreq = defaultdict(int)
        pre = 0
        subArrCount = 0

        for num in nums:
            pre += num

            if pre == goal:
                subArrCount += 1
            subArrCount += prefixFreq[pre - goal]

            prefixFreq[pre] += 1
        
        return subArrCount