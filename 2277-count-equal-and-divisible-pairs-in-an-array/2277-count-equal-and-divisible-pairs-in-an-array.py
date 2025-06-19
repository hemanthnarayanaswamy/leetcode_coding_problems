class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i != j and nums[i] == nums[j]:
                    if i*j % k == 0:
                        count += 1
        
        return count 