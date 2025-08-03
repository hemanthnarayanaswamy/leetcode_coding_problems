class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        pre = -k - 1    

        for i, v in enumerate(nums):
            if v == 1:
                if i - pre - 1 < k:
                    return False 
                pre = i
        
        return True