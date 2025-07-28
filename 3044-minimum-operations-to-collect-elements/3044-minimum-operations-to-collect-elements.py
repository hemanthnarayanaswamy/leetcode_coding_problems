class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        numsMap = {nu: i for i, nu in enumerate(nums)}
        idx = []

        for i in range(1, k+1):
            idx.append(numsMap[i])
        
        return len(nums) - min(idx)