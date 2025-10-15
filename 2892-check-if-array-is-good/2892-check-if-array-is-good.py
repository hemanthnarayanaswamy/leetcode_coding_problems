class Solution:
    def isGood(self, nums: List[int]) -> bool:
        numsMap = Counter(nums)
        n = len(numsMap)

        for i in range(1, n):
            if i not in numsMap or numsMap[i] != 1:
                return False
        
        if numsMap[n] != 2:
            return False
        
        return True
