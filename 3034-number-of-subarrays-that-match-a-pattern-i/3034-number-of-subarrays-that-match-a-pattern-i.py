class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)
        count = 0

        for i in range(n-m):
            valid = True
            for j in range(i, i+m):
                pat = pattern[j-i]
                n1, n2 = nums[j], nums[j+1]
                if pat == 0 and n1 != n2:
                    valid = False
                    break
                    
                if pat == 1 and n1 >= n2:
                    valid = False
                    break

                if pat == -1 and n1 <= n2:
                    valid = False
                    break
            if valid:
                count += 1
        
        return count
