class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        min_odd = min((x for x in nums1 if x % 2 == 1), default=float('inf'))
        min_even = min((x for x in nums1 if x % 2 == 0), default=float('inf'))


        if min_odd == float('inf') or min_even == float('inf'):
            return True
        
        flag = True 
        for i in range(n):
            if nums1[i] % 2 and nums1[i] - min_odd < 1:
                flag = False
                break
        
        if flag:
            return flag
        
        for i in range(n):
            if nums1[i] % 2 == 0 and nums1[i] - min_odd < 1:
                return False
        return True




        
