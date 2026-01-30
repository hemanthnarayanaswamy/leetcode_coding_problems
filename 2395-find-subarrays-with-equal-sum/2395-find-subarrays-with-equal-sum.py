class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        pairSum = set()

        for i in range(len(nums)-1):
            tmp = nums[i] + nums[i+1]
            if tmp in pairSum:
                return True
            pairSum.add(tmp)
        
        return False