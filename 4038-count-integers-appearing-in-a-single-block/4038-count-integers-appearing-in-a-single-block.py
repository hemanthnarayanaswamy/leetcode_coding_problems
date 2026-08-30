class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        count = 0 
        freq = Counter(nums)
        l = r = 0

        while r < len(nums):
            if nums[l] == nums[r]:
                r += 1
            else:
                if freq[nums[l]] == r - l:
                    count += 1
                l = r
        
        if freq[nums[l]] == r - l:
            count += 1

        return count
                

        
            
