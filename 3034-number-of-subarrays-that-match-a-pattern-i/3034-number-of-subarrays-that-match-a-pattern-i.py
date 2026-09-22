class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        n = len(nums)
        m = len(pattern)
        count = 0

        for i in range(n-m):
            valid = True
            for j in range(i, i+m):
                k = j - i
                pat = pattern[k]
                print(nums[j], nums[j+1])
                if pattern[k] == 0 and nums[j] != nums[j+1]:
                    valid = False
                    break
                    
                if pattern[k] == 1 and nums[j] >= nums[j+1]:
                    valid = False
                    break

                if pattern[k] == -1 and nums[j] <= nums[j+1]:
                    valid = False
                    break
            if valid:
                count += 1
        
        return count
