class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        tmp = []

        for i, v in enumerate(nums):
            if v == 1:
                tmp.append(i)
        
        for j in range(1, len(tmp)):
            if tmp[j] - tmp[j-1] - 1 < k:
                return False
        
        return True