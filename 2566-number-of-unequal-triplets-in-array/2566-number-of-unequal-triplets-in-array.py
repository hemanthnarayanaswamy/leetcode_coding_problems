class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)

        for i in range(n): 
            x = nums[i]
            for j in range(i+1, n): 
                y = nums[j]
                if x == y:
                    continue
                for k in range(j+1, n):
                    z = nums[k]
                    if x != z and y != z:
                        count += 1
        
        return count